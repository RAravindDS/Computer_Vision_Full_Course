""" 
What is Templeate Matching?
- A method of image matching that uses a template image to find a similar image in a larger image.
- The template image is a smaller image that is used to find a similar image in the larger image

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\Messi.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
templeate = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\messi_face3.png',0)

res = cv2.matchTemplate(gray_img, templeate, cv2.TM_CCOEFF_NORMED)
# cv2.matchTemplate(src, templ, method) 
# methods are more like cv2.TM_CCORR_NORMED, cv2.TM_CCORR, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED
print(res)

threshold = 0.8;
loc = np.where(res >= threshold)
print(loc)

w,h = templeate.shape[::-1] # column and rows in reverse order 

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2) # pt[0]+w - bottom right corner, pt[1]+h - top right corne, pt - top value. 


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

