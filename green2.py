import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import Deteccion as Det
import servomodulo as sm
import motormodulo as mm
global cap
cap =cv2.VideoCapture(0)
template = cv2.imread("/home/pi/Desktop/green-1.png", 0)
templateblue = cv2.imread("/home/pi/Desktop/blue-1.png", 0)
w, h = template.shape[::-1]
sm.setDirection(0)
sm.setDirection(120)
sm.setDirection(60)
rutina_1=True                
rutina_2=False
count=0
count1=0
count2=0
lock1=1
lock2=0
end=0
grub=True
if __name__ == '__main__':
    while grub:
        _, frame = cap.read()
        cv2.imshow("frame",frame)
        count=count+1
        print("count ",count)
        key = cv2.waitKey(1)
        if (key == 27) or (end ==1):
            mm.stop()
            break
       
        while (rutina_1==True and count>20):
            _, frame = cap.read()
            lower_color =np.array([63, 173, 52])
            upper_color= np.array([90, 255, 75])
            print("rutina verde")
            top_left,bottom_right,frame=Det.DeteccionRojo(frame,template,w,h,lower_color,upper_color)
            if top_left[0]!=0:
                sm.setDirection(90)
                rutina_2=True
                rutina_1=False
                count=0
                break
        while rutina_2==True and rutina_1==False and count>20:
            time.sleep(0.2)
            _, frame = cap.read()
            lower_color =np.array([68, 121, 00])
            upper_color= np.array([179, 255, 191])
            top_left_b,frame=Det.DeteccionBlue(frame,templateblue,w,h)
            print(top_left_b)
            count1=count1+1
            print("COUNT1",count1)
            if count1>10 and count2<=4 and lock1==1:
                mm.Dir_Centro_Izq()
                time.sleep(2)
                mm.stop()
                print("count2-1:",count2)
                count2=count2+1
                count1=0
                if top_left_b[0] > 20 :
                    print("break")
                    rutina_2=False
                    rutina_1=False
                    end =1
                    break
                if count2 ==4:
                    lock1=0
                    lock2=1
                    count2=0

            elif count1>10 and count2<=7 and lock2==1:
                mm.DirCentro_Der()
                
                time.sleep(2)
                mm.stop()
                count2=count2+1
                print("count2-2",count2)
                
                count1=0
                if top_left_b[0] != 0 :
                    print("break")
                    rutina_2=False
                    rutina_1=False
                    end =1
                    break
                if count2 ==6:
                    lock1=1
                    lock2=0
            key = cv2.waitKey(1)
            if key == 27:
                mm.stop()
                break
            
mm.PWMstop()
cv2.waitKey()
cv2.destroyAllWindows()