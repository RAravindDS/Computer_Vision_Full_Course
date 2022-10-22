import cv2 
import numpy as  np 

""" 
Contours can be expalined as the curve joining all the continous point along the boundary which are the same color intensity. 
Contours can be used for shape analysis, object detection or objecty recognition. 
For better accuracy we generally use binary images. 
Before finding out the controus we are going to apply threshold or canny edge detection to find the contors in the image.  
Contours is a python list of all the contorus in a image. Each individual contour is a numpy array of (x,y) coordinates of boundary points of the object.
"""

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

ret, thresh = cv2.threshold(imgray, 127, 255, 0) # 127 half of the 255 right? 

# to find the contours. 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cv2.findcontrous(threshold value, contour mode, method (contour approximation method)) 
print("Number of Contours = "+str(len(contours)))

# To draw the contours we can use this 
cv2.drawContours(img, contours,-1, (0, 255, 0), 3) # -1 means all the contours, 3 is the thickness of the line 
#cv2.drawContours(img, contours,0, (0, 255, 0), 3) # 0 means first the contours, 3 is the thickness of the line 

#cv2.drawcontorus(image, contours, contour index, color, thickness)

cv2.imshow('image', img) 
cv2.imshow('gray_image', imgray) 
cv2.waitKey(0)
cv2.destroyAllWindows() 



