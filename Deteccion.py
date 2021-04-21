import cv2
import numpy as np
def DeteccionRojo(frame,template,width, height,lower_color,upper_color):
    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.matchTemplate(mask, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)
    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    return (top_left,bottom_right)
    

def DeteccionVerde(frame,template,width, height):
    lower_color =np.array([41, 81, 54])
    upper_color= np.array([86, 244, 118])
    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.matchTemplate(mask, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow("frame",frame)
    return (top_left,bottom_right,frame)

def DeteccionBlue(frame,template,width, height):
    lower_color =np.array([89, 121, 00])
    upper_color= np.array([179, 255, 191])
    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.matchTemplate(mask, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(frame, top_left, bottom_right, (0, 00, 255), 2)
    cv2.imshow("frame",frame)
    return (top_left,frame)