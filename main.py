import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import Deteccion as Det
import servomodulo as sm
import motormodulo as mm
import greenModulo as gm
global cap
cap =cv2.VideoCapture(0)
template = cv2.imread("/home/pi/Desktop/red-line11.PNG", 0)
w, h = template.shape[::-1]
sm.setDirection(90)
sm.setDirection(0)
sm.setDirection(65)
rutina=True
rutina_1=False                
rutina_2=False
cred=0
clok=0
count=0
lok=1
if __name__ == '__main__':
    while rutina==True :
        key = cv2.waitKey(1)
        if key == 27:
            mm.stop()
            break
        _, frame = cap.read()
        lower_color =  np.array([00, 136, 78])
        upper_color=np.array([255, 255,168])
        count=count+1
        if count== 3:
            cred=cred+1
            clok=clok+1
            count=0
        ROI = frame[249:638,2:638]
        top_left,bottom_right=Det.DeteccionRojo(ROI,template,w,h,lower_color,upper_color)
        #print("top_left[]0",top_left[0])
        print("conteo",cred)
        if top_left[0]>230 and bottom_right[0]<400:
            mm.DirC()
        if top_left[0]>5 and top_left[0]<230 :
            mm.DirIz()
        if top_left[0]==0 and lok==1:
            mm.stop()
            
            if cred>=0 and cred<=3 :
                mm.DirIz()
                if top_left[0]!=0:
                    cred=0
            if cred>=4 and cred<=7 :
                mm.DirDe()
                if top_left[0]!=0:
                    cred=0
            if cred>=8 and cred<=10:
                mm.DirRev()
                if top_left[0]!=0 :
                    cred=0
        if cred ==10 or cred >10:
            cred=0
        if clok>=2:
            lok1=0
            clok=0
        if bottom_right[0]>400:
            mm.DirDe()
    while rutina_1==True :
        mm.stop()
        _, frame = cap.read()
        top_left_G,rutina_1,rutina_2=gm.rutina_1(frame,rutina_1,rutina_2)
        if top_left_G[0]!=0 and clok>=1:
            lok1=0
            rutina_1=True
            rutina=False
            print("verde encontrado")
            break
        elif clok>=2:
            lok1=1
            rutina_1=False
            rutina=True
            print("no verde ")
            break
        
   #and top_left_G!=0
mm.PWMstop()
cv2.waitKey()
cv2.destroyAllWindows()