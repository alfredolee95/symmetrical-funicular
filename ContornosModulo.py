import cv2
import numpy as np
areaProm=[]
avgVal=10
ret=True
def nothing(x):
    pass
def contorno(frame):
    lower_color =np.array([80, 100, 44])
    upper_color= np.array([148, 231, 150])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    blurred_frame = cv2.GaussianBlur(mask, (5, 5), 0)
    laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    canny = cv2.Canny(blurred_frame, 100, 300)
    _, ctns, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, ctns, -1, (0,0,255), 2)
    prom=len(ctns)
    areaProm.append(prom)
    if len(areaProm)>avgVal:
        areaProm.pop(0)
    contorno=int(sum(areaProm)/len(areaProm))
    #print(contorno)
    print('Número de contornos encontrados: ', contorno)
    #cv2.imshow('Imagezn', frame)
    #cv2.imshow('Imagen', laplacian)
    #cv2.imshow('canny',canny)
    cv2.imwrite('/home/pi/Desktop/version en modulos/canny.png', canny)
    return (contorno,frame)


cv2.waitKey(0)
cv2.destroyAllWindows()