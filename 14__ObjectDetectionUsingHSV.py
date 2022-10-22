""" There are more than 150 types of changing the BGR to another type, one of the  type is HSV 
HSV (Hue, Saturation, Value) is the most common color space used for color detection and recognition. 
It is also stand hexagon color model""" 

""" Hue corresponds to the color compoenent of the color. selecting a range of hue you can select various color(0-360)) 
    Saturation is amount of color in the image (depth of the image) (0 - 100%) 
    Value is basically the brightness of the color (0 - 100%) """


import cv2 
import numpy as np 

def nothing(x): 
    print(x)
cap = cv2.VideoCapture(0); 

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing) # lower hue (LH) 
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing) # lower saturation (LS) 
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing) # lower value (LV)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing) # upper hue (UH)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing) # upper saturation (US)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing) # upper value (UV)


while True: 
    #frame = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\smarties.png') 
    _, frame = cap.read() 
    # ___________________________________________________________________________________________# 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    """ I want to detect only blue color"""
    #_______________________________________________________________________________________________# 

    

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking') 


    l_b = np.array([l_h,l_s,l_v]) # In order to find lower and upper bounds, you can use the trackbar. 
    u_b = np.array([u_h,u_s,u_v])    # lower bound and upper bound

    mask = cv2.inRange(hsv, l_b, u_b) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res) 
    key = cv2.waitKey(1) & 0xFF

    if key == 27: 
        break 

cap.release()
cv2.destroyAllWindows()