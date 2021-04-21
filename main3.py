import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import Deteccion as Det
import servomodulo as sm
import motormodulo as mm
import posicion_momentum_color as pmc
global cap
cap =cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_FPS,60)
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
        ROI1 = frame[336:638,2:638]
        #ROI2 = frame[212:333,2:640]
        lower_color= np.array([00, 115, 105])
        upper_color= np.array([255, 255,255])
        frame,sd=pmc.deteccion_color(frame,lower_color,upper_color)
        cv2.drawContours(frame, sd, 0, (255,0,0), 3)
        cv2.imshow("frame",frame)
        #lower_color =  np.array([161, 136, 78])
        #upper_color=np.array([255, 255,168])
        
mm.PWMstop()
cv2.waitKey()
cv2.destroyAllWindows()