import cv2 
import numpy as np 

def click_event(event, x,y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        """ I am going to draw a circle when I click left button """
        cv2.circle(img, (x,y), 4, (0,0,255), -1) # img, coordinate, radius, color, thickness 
        points.append((x,y)) # append the coordinate to the list 
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0,255,0), 5)

        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN: 
        """ I want to bring a new window of the color what I am touching in the photo"""
        blue = img[y,x, 0] # Channel for blue is 0
        green = img[y,x,1] # Channel for green is 1
        red = img[y,x,2] # Channel for red is 2

        cv2.circle(img, (x,y), 4, (0,0,255), -1) # img, coordinate, radius, color, thickness
        mycolorImage = np.zeros((512,512,3), np.uint8) # create a black image
        mycolorImage[:] = [blue, green, red] # set the color of the image
        cv2.imshow('color', mycolorImage)
        

#img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png', -1)
img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)
points = [] 

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 

