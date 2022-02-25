import cv2 as cv
import pytesseract
from pyfirmata import Arduino, SERVO
from time import sleep


pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


port='COM6'

pin1=10 #en alttaki
pin2=5 #ortak eksen 
pin3=5
pin4=6
pin5=9
pin6=11  # tutma kısmı


board = Arduino(port)
board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
board.digital[pin3].mode = SERVO
board.digital[pin4].mode = SERVO
board.digital[pin5].mode = SERVO
board.digital[pin6].mode = SERVO
 
board.digital[pin6].write(0)
sleep(0.015)
board.digital[pin2].write(90)
board.digital[pin3].write(90)
sleep(0.015)

board.digital[pin5].write(45)
sleep(0.015)

board.digital[pin4].write(0)

board.digital[pin1].write(0)

sleep(0.017)




cap = cv.VideoCapture(0) # kamera 0 pc kamerası  1 diğer kamera

# kameradan fotoğraf çekme kısmı
while cap.isOpened():
             kontrol, frame = cap.read()
             resim=cv.imwrite("fff.jpg",frame)
             cv.imread('resim')
             cv.imshow("or",kontrol)
             resim = cv.imread('fff.jpg')

             metin = pytesseract.image_to_string(resim)
             metin = ''.join(metin.split())

             print(metin)

             cv.imshow("resim", resim)
             if cv.waitKey(2)&0xFF==ord('q'):
                 break
cap.release()
cv.destroyAllWindows()


# servo motoru konuma götürme fonksiyonu
def rotateServo(pin, angle):
    
    
        board.digital[pin].write(angle)
        
        sleep(0.03)
    
    

   
#tutma kısmı (algılandıktan sonra bu fonksiyona giriyor)
def tutma():
    
    sleep(0.03)
    
    for i in range(45,60,1):
         
         rotateServo(pin5, i) 
         
    sleep(0.03)
    
    for i in range(0,45,1):
         
         rotateServo(pin4, i)
         
         
    sleep(0.3)     
    for i in range(0,90,1):
          
          rotateServo(pin6,i)
          
    sleep(0.03)
    
    
    for i in range(60,80,1):
           
          rotateServo(pin5,i)      
    
    sleep(0.3)  

    for i in range(45,30,-1):
          
          rotateServo(pin4, i)
          
          
    
def bırakma():
    
         
    for i in range(80,60,-1):
            
          rotateServo(pin5,i)    
          
    sleep(0.3) 
        
    for i in range(30,45,1):
          
          rotateServo(pin4, i)
          
    sleep(0.3)      
    for i in range(90,0,-1):
          
          rotateServo(pin6,i)
          
    sleep(0.3)
         
   
    for i in range(60,80,1):
             
           rotateServo(pin5,i) 
    

if metin[0:11]=="ASMALIEVLER":
    
    print("ASMALIEVLER KARGOSU ALGILANDI")
    
    tutma()
    
    sleep(0.03)
    
    for i in range(0,90,1):
           
          rotateServo(pin1,i)
      
    sleep(0.3)
    
    bırakma()
    
           

          
elif metin[0:9]=="YUNUSEMRE":
    
        print("YUNUSEMRE KARGOSU ALGILANDI")
        tutma()
        
        sleep(0.03)
        
        for i in range(0,180,1):
               
              rotateServo(pin1,i)
          
        sleep(0.3)
        
        bırakma()
   
else:
     print("okuma yapılamadı")