import cv2 
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('D:\\Learning_ML_Krish\\Computer_Vision\\images\\smarties.png')
"""
( x - x centr )^2 + ( y - y centr )^2 = r^2 - It is a circle equation. 

"""

output = img.copy() 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5) # Hough circle works well in blurred images.
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# cv2.hougcircles(img,method,dp,minDist,param1,param2,minRadius,maxRadius)
""" 
Method - Only one method is availabe is Hough_Gradient method. 
dp - Inverse ratio of accumulator resolution to image resolution.For example: dp=1 means 1 pixel per accumulator cell and it has .5 height and .5 width. (Half of the input)
mindist - Minimum distance between center of the detected circles. 
param1 - `Gradient value` in x-direction.
param2 - `Gradient value` in y-direction. 
minradius - Minimum circle radius.
maxradius - Maximum circle radius.
The output of this will be a vector. 
"""

detected_circles = np.int16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)
    cv2.circle(output, (x,y), 2, (0, 255, 255),3) 


cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()