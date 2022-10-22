import cv2 
import numpy as np 

""" Trackbar are really usefull whenever you want to change the value in image, dynamically at runtime"""

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image') # It helps to create a window with name 

def nothing(x):
    print(x) 

cv2.createTrackbar('B', 'image', 0, 255, nothing) # it helps to change the blue channel of image
# createtrackbar(unique name, name of the window, initial value, max value, callback function)
cv2.createTrackbar('G', 'image', 0, 255, nothing) # it helps to change the green channel of the image. 
cv2.createTrackbar('R', 'image', 0, 255, nothing) # it helps to change the red channel of the image.

# if you want to add swith button then use this code:
switch = '0: OFF \n 1: ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing) 

while True: 
    cv2.imshow('image', img)

    K = cv2.waitKey(1) & 0xFF
    if K == 27: # Escape key 
        break

    b = cv2.getTrackbarPos('B', 'image') # it helsp to get the values 
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image') 
    s = cv2.getTrackbarPos(switch, 'image') 

    
    
    if s == 0: 
        img[:] = 0
    else:
        img[:] = [b, g, r]


cv2.destroyAllWindows()