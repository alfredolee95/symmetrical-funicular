import cv2
import numpy as np
cap =cv2.VideoCapture(0)
areaProm=[]
avgVal=20
ret=True
def nothing(x):
    pass
def fillhole(input_image):
    im_flood_fill = input_image.copy()
    h, w = input_image.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    im_flood_fill = im_flood_fill.astype("uint8")
    cv2.floodFill(im_flood_fill, mask, (0, 0), (255,255,255))
    im_flood_fill_inv = cv2.bitwise_not(im_flood_fill)
    img_out = input_image | im_flood_fill_inv
    return img_out
while ret==True:
    key = cv2.waitKey(1)
    if (key == 27):
        break
    _, frame = cap.read()
    lower_color =np.array([100, 60, 50])
    upper_color= np.array([226, 130, 88])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, lower_color, upper_color)
    mask=fillhole(mask1)
    blurred_frame = cv2.GaussianBlur(mask, (5, 5), 0)
    laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    canny = cv2.Canny(blurred_frame, 250, 300)
    _, ctns, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, ctns, -1, (0,0,255), 2)
    #suavisa cantidad de resultados /promedia valores
    prom=len(ctns)
    areaProm.append(prom)
    if len(areaProm)>avgVal:
        areaProm.pop(0)
    contorno=int(sum(areaProm)/len(areaProm))
    print(contorno)
    #print('Número de contornos encontrados: ', len(ctns))

    #texto = 'Contornos encontrados: '+ str(len(ctns))
    #cv2.putText(frame, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 0, 0), 1)
    cv2.imshow('frame', frame)
#    cv2.imshow('mask',mask)
#    cv2.imshow('laplacian', laplacian)
    cv2.imshow('canny',canny)
    key = cv2.waitKey(1)
    if (key == 27):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()