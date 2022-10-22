import cv2 
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('D:\\Learning_ML_Krish\\Computer_Vision\\images\\road.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # It is preferred to have a grayscale image in canny edge detection. 

edges = cv2.Canny(gray, 50, 150, apertureSize = 3) # apertureSize = 3 is the default value, 50 and 150 are the lower and upper thresholds.
cv2.imshow('edges', edges)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength= 100, maxLineGap= 10) # 1 - rho, np.pi/180 - theta, 200 - threshold 

"""
Threshold - Acculumator threshold parameter. Only those lines are returned that get enough votes ( > threshold).
minLineLength - Minimum line length. Line segments shorter than that are rejected.( Other words, line which lesser than the values will be rejected)
maxLineGap - Maximum allowed gap between points on the same line to link them. (Other words, maximum allowded gap, we have given)
"""

for line in lines: 
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2) # (x1, y1) - start point, (x2, y2) - end point, (0, 0, 255) - color, 2 - thickness

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


