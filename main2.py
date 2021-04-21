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
        lower_color =  np.array([00, 108, 96])
        upper_color=np.array([186, 193,139])
        count=count+1
        if count== 3:
            cred=cred+1
            clok=clok+1
            count=0
        #top_left,bottom_right,frame=Det.DeteccionRojo(frame,template,w,h,lower_color,upper_color)
        #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame, lower_color, upper_color)
        _,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame, contornos, -1, (255,0,0), 1)
        for c in contornos:
            area = cv2.contourArea(c)
            #areaProm.append(area)
            #if len(areaProm)>avgVal:
            #    areaProm.pop(0)
            #area=int(sum(areaProm)/len(areaProm))
            #if area <1499: area==0
            if area > 1500:
                print(area)
                M = cv2.moments(c)
                if (M["m00"]==0): M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int(M['m01']/M['m00'])
                cv2.circle(frame, (x,y), 7, (0,255,0), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                #cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)
                cv2.imshow('frame',frame)
        #print("conteo",cred)
        if x>230 and x<400:
            mm.DirC()
        if x>5 and x<230 :
            mm.DirIz()
        if x==0 and lok==1:
            mm.stop()
        if x>400:
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