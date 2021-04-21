import cv2
import numpy as np
def deteccion_color(frame,lower_color,upper_color):
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,lower_color,upper_color)
    _,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contornos, -1, (255,0,0), 1)
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 3000:
            M = cv2.moments(c)
            if (M["m00"]==0): M["m00"]=1
            x = int(M["m10"]/M["m00"])
            y = int(M['m01']/M['m00'])
            cv2.circle(frame, (x,y), 7, (0,255,0), -1)
            #font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
            nuevoContorno = cv2.convexHull(c)
#             cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)
            return (frame,nuevoContorno)
