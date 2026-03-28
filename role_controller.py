import time
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

loc = r"/home/pi/Desktop/Program/role_urls"

button_1 =  9
button_2 =  10 
button_3 =  11
button_4 =  12
button_5 =  13
button_6 =  16
button_7 =  17
button_8 =  18
button_9 =  19
button_10 =  20
button_11 =  21
button_12 =  22
button_13 =  23
button_14 =  24
button_15 =  25
button_16 =  26

GPIO.setup(button_1,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_2,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_5,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_6,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_7,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_8,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_9,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_10,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_11,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_12,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_13,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_14,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_15,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_16,GPIO.IN,pull_up_down = GPIO.PUD_UP)

BS1 = False
BS2 = False
BS3 = False
BS4 = False
BS5 = False
BS6 = False
BS7 = False
BS8 = False
BS9 = False
BS10 = False
BS11 = False
BS12 = False
BS13 = False
BS14 = False
BS15 = False
BS16 = False

def gonder(url):
    try:
        requests.get(url, timeout=0.5)
    except:
        print("Doğru IP Girmelisiz. Lütfen IP değiştirme programına girip değişiklik yapınız.")

while(1):    
    try:
        with open(loc, 'r') as file :
            filedata = file.read()
            urls = filedata.split(' , ')
    except:
        print("URL dosyası okunamadı.")
        continue

    if GPIO.input(button_1)==0:
        if BS1==False:
            gonder(urls[0])
            BS1=True
            print("Buton 1 is OPEN")

    if GPIO.input(button_1)==1:
        if BS1==True:
            gonder(urls[16])
            BS1 = False
            print("Buton 1 is CLOSE")
 	  
    if GPIO.input(button_2)==0:
        if BS2==False:
            print("Buton 2 is OPEN")
            gonder(urls[1])
            BS2 = True

    if GPIO.input(button_2)==1:
        if BS2==True:
            print("Buton 2 is CLOSE")
            gonder(urls[17])
            BS2 = False

    if GPIO.input(button_3)==0:
        if BS3==False:
            print("Buton 3 is OPEN")
            gonder(urls[2])
            BS3 = True

    if GPIO.input(button_3)==1:
        if BS3==True:
            print("Buton 3 is CLOSE")
            gonder(urls[18])
            BS3 = False

    if GPIO.input(button_4)==0:
        if BS4==False:
            print("Buton 4 is OPEN")
            gonder(urls[3])
            BS4 = True

    if GPIO.input(button_4)==1:
        if BS4==True:
            print("Buton 4 is CLOSE")
            gonder(urls[19])
            BS4 = False
            
    if GPIO.input(button_5)==0:
        if BS5==False:
            print("Buton 5 is OPEN")
            gonder(urls[4])
            BS5 = True

    if GPIO.input(button_5)==1:
        if BS5==True:
            print("Buton 5 is CLOSE")
            gonder(urls[20])
            BS5 = False
          
    if GPIO.input(button_6)==0:
        if BS6==False:
            print("Buton 6 is OPEN")
            gonder(urls[5])
            BS6 = True
 
    if GPIO.input(button_6)==1:
        if BS6==True:
            print("Buton 6 is CLOSE")
            gonder(urls[21])
            BS6 = False

    if GPIO.input(button_7)==0:
        if BS7==False:
            print("Buton 7 is OPEN")
            gonder(urls[6])
            BS7 = True

    if GPIO.input(button_7)==1:
        if BS7==True:
            print("Buton 7 is CLOSE")
            gonder(urls[22])
            BS7 = False

    if GPIO.input(button_8)==0:
        if BS8==False:
            print("Buton 8 is OPEN")
            gonder(urls[7])
            BS8 = True

    if GPIO.input(button_8)==1:
        if BS8==True:
            print("Buton 8 is CLOSE")
            gonder(urls[23])
            BS8 = False

    if GPIO.input(button_9)==0:
        if BS9==False:
            print("Buton 9 is OPEN")
            gonder(urls[8])
            BS9 = True
  
    if GPIO.input(button_9)==1:
        if BS9==True:
            print("Buton 9 is CLOSE")
            gonder(urls[24])
            BS9 = False

    if GPIO.input(button_10)==0:
        if BS10==False:
            print("Buton 10 is OPEN")
            gonder(urls[9])
            BS10 = True

    if GPIO.input(button_10)==1:
        if BS10==True:
            print("Buton 10 is CLOSE")
            gonder(urls[25])
            BS10 = False

    if GPIO.input(button_11)==0:
        if BS11==False:
            print("Buton 11 is OPEN")
            gonder(urls[10])
            BS11 = True
     
    if GPIO.input(button_11)==1:
        if BS11==True:
            print("Buton 11 is CLOSE")
            gonder(urls[26])
            BS11 = False
        
    if GPIO.input(button_12)==0:
        if BS12==False:
            print("Buton 12 is OPEN")
            gonder(urls[11])
            BS12 = True
      
    if GPIO.input(button_12)==1:
        if BS12==True:
            print("Buton 12 is CLOSE")
            gonder(urls[27])
            BS12 = False
 
    if GPIO.input(button_13)==0:
        if BS13==False:
            print("Buton 13 is OPEN")
            gonder(urls[12])
            BS13 = True
        
    if GPIO.input(button_13)==1:
        if BS13==True:
            print("Buton 13 is CLOSE")
            gonder(urls[28])
            BS13 = False
            
    if GPIO.input(button_14)==0:
        if BS14==False:
            print("Buton 14 is OPEN")
            gonder(urls[13])
            BS14 = True
          
    if GPIO.input(button_14)==1:
        if BS14==True:
            print("Buton 14 is CLOSE")
            gonder(urls[29])
            BS14 = False
          
    if GPIO.input(button_15)==0:
        if BS15==False:
            print("Buton 15 is OPEN")
            gonder(urls[14])
            BS15 = True
          
    if GPIO.input(button_15)==1:
        if BS15==True:
            print("Buton 15 is CLOSE")
            gonder(urls[30])
            BS15 = False
        
    if GPIO.input(button_16)==0:
        if BS16==False:
            print("Buton 16 is OPEN")
            gonder(urls[15])
            BS16 = True
  
    if GPIO.input(button_16)==1:
        if BS16==True:
            print("Buton 16 is CLOSE")
            gonder(urls[31])
            BS16 = False
