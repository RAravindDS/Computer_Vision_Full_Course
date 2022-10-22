import cv2 
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\sudoku.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # It is preferred to have a grayscale image in canny edge detection. 

edges = cv2.Canny(gray, 50, 150, apertureSize = 3) # apertureSize = 3 is the default value, 50 and 150 are the lower and upper thresholds.
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200) # 1 - rho, np.pi/180 - theta, 200 - threshold
""" 
rho - distance resolution in pixels of the accumulator in pixel. 
theta - angle resolution in radians of the accumulator in radians. 
threshold - accumulator threshold parameter. Only those lines are returned that get enough votes ( > threshold).
- It will return a output vector of a lines. Each line is represented by a vector of two points.
"""

for line in lines: 
    rho, theta = line[0] # line[0] is a vector of two points, It will give the rho and theta values.
    a = np.cos(theta) # the formula for the polar coordinates is rho = x*cos(theta) + y*sin(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho 
    # Once you get the x and y value, you can use this equation to get the line ( r * cos (theta) - 1000 * sin (theta) ): r - represent rows, theta - represent columns.
    x1 = int(x0 + 1000*(-b))
    # y1 stores the rounded off value of ( r * sin (theta) + 1000 * cos (theta) ): r - represent rows, theta - represent columns.
    y1 = int(y0 + 1000*(a)) 
    # x2 stores the rounded off value ( r * cos(theta) + 1000 * sin (theta) ): r - represent rows, theta - represent columns.'
    x2 = int(x0 - 1000*(-b))
    # y2 stores the rounded off value ( r * sin (theta) - 1000 * cos (theta) ): r - represent rows, theta - represent columns.
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2) # (x1, y1) - start point, (x2, y2) - end point, (0, 0, 255) - color, 2 - thickness


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" 
The Problemm is that the lines are not having any end. To overcome this we will use Problastice Hough Transform Function. 
"""