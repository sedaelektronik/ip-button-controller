# Kod ile Kullanılabilir Seda Elektronik Ürünleri: 
# https://sedaelektronik.com.tr/ip-button-16.html
# https://sedaelektronik.com.tr/ip-button-4.html
# https://sedaelektronik.com.tr/internetten-role-cihaz-kontrol.html
#!/usr/bin/env python
import os
# Dosyanın bulunduğu klasörü bulur
current_dir = os.path.dirname(os.path.abspath(__file__))
loc = os.path.join(current_dir, "role_urls")
# Resim yollarını da buna göre güncelle:
# on_img = PhotoImage(file=os.path.join(current_dir, "on.png"))
import tkinter
from tkinter import *
from PIL import Image, ImageTk #ImageTK hatası için terminale şu kodun girilmesi gerekmektedir. sudo apt-get install
from tkinter import messagebox
import requests
import threading  # Eklendi
from tkinter import ttk
import sys
import re
# import RPi.GPIO as GPIO #rpde aç - Alt satıra taşındı

# windows 3.13 py ide için örnek lib yükleme:
#py -3.13 -m pip install Pillow

# Windows Simülasyonu pin taklit satırıları satır 17-23
#if sys.platform == "win32":
#    from unittest.mock import MagicMock
#    mock_gpio = MagicMock()
#    mock_gpio.input.return_value = 1 
#    mock_gpio.BCM = "BCM"
#    mock_gpio.IN = "IN"
#    mock_gpio.PUD_UP = "PUD_UP"
#    sys.modules["RPi.GPIO"] = mock_gpio

#raspberry de 2 alttaki 2 satırı aç:
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except Exception as e:
    print(f"GPIO Hatası: {e}") # Yetki hatası varsa terminale yazar ama arayüzü açar

root = Tk()
root.title("SEDA ELEKTRONİK - 12'Lİ ÇOKLU KONTROL")
root.geometry("750x900")

# Sekme Yapısı
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15, fill="both", expand=True)

my_frame_2 = Frame(my_notebook, width=750, height=850) # Röle Kontrol (Sekme 1)
my_frame_1 = Frame(my_notebook, width=750, height=850) # IP Düzenleme (Sekme 2)

my_frame_1.pack(fill="both", expand=1)
my_frame_2.pack(fill="both", expand=1)

#my_notebook.add(my_frame_2, text="RELAY/BUTON KONTROL")
my_notebook.add(my_frame_1, text="KONTROL IP DÜZENLEME")

loc = r"./role_urls"
relay_states = [False] * 16
ip_entries = []

# --- IP DÜZENLEME SEKMESİ (Frame 1) ---
# 12 IP için kaydırma çubuğu gerekebileceği düşünülerek yerleşim sıkılaştırıldı
Label(my_frame_1, text="12 CİHAZLI IP YAPILANDIRMASI", font=("Arial", 14, "bold")).pack(pady=10)

# IP Girişlerini oluştur (12 Adet)
for i in range(12):
    f = Frame(my_frame_1)
    f.pack(pady=2)
    Label(f, text=f"Cihaz {i+1} IP:", width=12, anchor="w").pack(side=LEFT)
    ent = Entry(f, width=25, font=("Arial", 11), justify="center")
    ent.pack(side=LEFT)
    ent.insert(0, "10.10.10.231") # Varsayılan değer
    ip_entries.append(ent)

def check_saved_ips():
    """Program açıldığında dosyadaki IP'leri kutucuklara doldurur."""
    try:
        with open(loc, 'r') as file:
            content = file.read()
            # Dosyadaki tüm URL'leri ayır
            urls = content.split(' , ')
            
            # İlk 12 rölenin ON komutları ilk 12 sırada olduğu için
            # doğrudan bu URL'lerden IP'leri ayıklıyoruz
            temp_ips = []
            for i in range(12):
                match = re.search(r'http://([\d\.]+):3000', urls[i])
                if match:
                    temp_ips.append(match.group(1))
            
            # Arayüzdeki kutucukları güncelle
            for i in range(len(temp_ips)):
                ip_entries[i].delete(0, END)
                ip_entries[i].insert(0, temp_ips[i])
    except Exception as e:
        print(f"Yükleme hatası: {e}")
        pass

def generate_urls():
    ips = [ent.get() for ent in ip_entries]
    keys = ['w','w','w','w','m','m','m','m','9','0','a','b','c','d','e','L', # çoklu ip röle kartlarına göre değiştiriniz 
            'n','n','n','n','t','t','t','t','o','p','q','t','u','v','w','M'] 
            # bütün parametreler: 
            #https://sedaelektronik.com.tr/ai-ml.html#python-api-main
    on_urls = []
    off_urls = []
    
    # 16 Röle için URL üretimi
    for i in range(16):
        # 1-12. Röleler kendi IP'sine, 13-16. Röleler 12. IP'ye (index 11)
        target_ip_index = i if i < 12 else 11
        current_ip = ips[target_ip_index]
            
        on_urls.append(f"http://{current_ip}:3000/{keys[i]}")
        off_urls.append(f"http://{current_ip}:3000/{keys[i+16]}")
        
    final_list = on_urls + off_urls
    return " , ".join(final_list)

def change_ip():
    try:
        data = generate_urls()
        with open(loc, 'w') as f:
            f.write(data)
        messagebox.showinfo("Başarılı", "12 Cihaz IP'si kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Kaydedilemedi: {e}")

Button(my_frame_1, text="AYARLARI KAYDET", bg="red", fg="white", font=("Arial", 12, "bold"), command=change_ip).pack(pady=15)

# --- RÖLE KONTROL SEKMESİ (Frame 2) ---
try:
    on_img = PhotoImage(file=r"./on.png")
    off_img = PhotoImage(file=r"./off.png")
except:
    on_img = None
    off_img = None

relay_buttons = []
relay_labels = []

def button_click(idx):
    def gonder():
        try:
            with open(loc, 'r') as f:
                urls = f.read().split(' , ')

            if not relay_states[idx]: # AÇMA
                requests.get(urls[idx], timeout=0.5)
                relay_buttons[idx].config(image=on_img)
                relay_labels[idx].config(fg="green")
                relay_states[idx] = True
            else: # KAPAMA
                requests.get(urls[idx+16], timeout=0.5)
                relay_buttons[idx].config(image=off_img)
                relay_labels[idx].config(fg="red")
                relay_states[idx] = False
        except Exception:
            pass  # Ulaşılamıyorsa sessizce geç, arayüz kilitlenmesin

    threading.Thread(target=gonder, daemon=True).start()

# 16 Röle Butonu Oluşturma
for i in range(16):
    col = 0 if i < 8 else 1
    row_idx = i if i < 8 else i - 8
    
    lbl = Label(my_frame_2, text=f"RELAY {i+1}", font=("Arial", 10, "bold"), fg="red")
    lbl.place(x=50 + (col*350), y=100 + (row_idx*60))
    relay_labels.append(lbl)
    
    btn = Button(my_frame_2, image=off_img, bd=0, command=lambda x=i: button_click(x))
    btn.place(x=150 + (col*350), y=95 + (row_idx*60))
    relay_buttons.append(btn)

# Başlangıçta verileri çek
check_saved_ips()

root.mainloop()
