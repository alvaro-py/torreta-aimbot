# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from servomove import servopos
ser=servopos()
import serial
dev = serial.Serial("/dev/ttyUSB2",115200)
import time
import pygame
import random
p=11



face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


Px,Ix,Dx=-1/160,0,0
Py,Iy,Dy=-0.2/120,0,0
integral_x,integral_y=0,0
differential_x,differential_y=0,0
prev_x,prev_y=0,0

width,height=320,240
camera = PiCamera()
camera.resolution = (width,height)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(width,height))
time.sleep(1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    frame=cv2.flip(image,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    

    ser.setdcx(0)
    ser.setdcy(0)
    
    #detect face coordinates x,y,w,h
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    c=0


     

    for(x,y,w,h) in faces:
        c+=1
        if(c>1):
            break
        #centre of face
        face_centre_x=x+w/2
        face_centre_y=y+h/2
        #pixels to move 
        error_x=160-face_centre_x
        error_y=120-face_centre_y
        
        integral_x=integral_x+error_x
        integral_y=integral_y+error_y
        
        differential_x= prev_x- error_x
        differential_y= prev_y- error_y
        
        prev_x=error_x
        prev_y=error_y
        
        valx=Px*error_x +Dx*differential_x + Ix*integral_x
        valy=Py*error_y +Dy*differential_y + Iy*integral_y
        
        
        valx=round(valx,1)
        valy=round(valy,1)

	

        print('pixelerrorx=',error_x,'valx=',valx)
        print('pixelerrory=',error_y,'valy=',valy)
        #p= p + 1

        if p >10:
          s = random.randint(1, 6)
          if s==1:
               pygame.init()
               pygame.mixer.init()
               sounda= pygame.mixer.Sound("blanco_fijado.wav")
               sounda.play()
               p = 0
          if s==2:
               pygame.init()
               pygame.mixer.init()
               sounda= pygame.mixer.Sound("hola.wav")
               sounda.play()
               p = 0
          if s==3:
               pygame.init()
               pygame.mixer.init()
               sounda= pygame.mixer.Sound("objetivo a la vista.wav")
               sounda.play()
               p = 0
          if s==4:
               pygame.init()
               pygame.mixer.init()
               sounda= pygame.mixer.Sound("rastreando.wav")
               sounda.play()
               p = 0
          if s==5:
               pygame.init()
               pygame.mixer.init()
               sounda= pygame.mixer.Sound("te encontre.wav")
               sounda.play()
               p = 0
          if s==6:
               pygame.init()
               pygame.mixer.init()
               sounda= pygame.mixer.Sound("te pille.wav")
               sounda.play()
               p = 0
          if s==7:
               pygame.init()
               pygame.mixer.init()
               sounda= pygame.mixer.Sound("te veo.wav")
               sounda.play()
               p = 0
          



        if error_y>0:
            dev.write("2 ".encode('ascii'))
            p= p + 1
            time.sleep(0.2)
        else: 
          if error_y<0:
            dev.write("1 ".encode('ascii'))
            p= p + 1
            time.sleep(0.2)


        if error_x>0:
            dev.write("3 ".encode('ascii'))
            p= p + 1
            time.sleep(0.2)
        else: 
          if error_x<0:
             dev.write("4 ".encode('ascii'))
             p= p + 1
             time.sleep(0.2)




        #cad = str(error_y+30) + "," + str(error_x-30)
        #dev.write(cad.encode('ascii'))
      

        if abs(error_x)<20:
            ser.setdcx(0)
        else:
            if abs(valx)>0.5:
                sign=valx/abs(valx)
                valx=0.5*sign
            ser.setposx(valx)

        if abs(error_y)<20:
            ser.setdcy(0)
        else:
            if abs(valy)>0.5:
                sign=valy/abs(valy)
                valy=0.5*sign
            ser.setposy(valy)
            
        if(c==1):
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),6)

    cv2.imshow('frame',frame) #display image
    
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break

cv2.destroyAllWindows()