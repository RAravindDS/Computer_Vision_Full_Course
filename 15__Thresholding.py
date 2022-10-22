import cv2 as cv
import numpy as np 
# Futher click this https://colab.research.google.com/github/YashviP/Computer-Vision-Playlist/blob/main/OpenCV/Image_Thresholding.ipynb#scrollTo=nVYmWkqdBZHj

""" It helps to seperating the object from bakcground, the process involve comparing each pixel of the image with pre
defind threshold value.  This process divide the input image into two groups, pixel having intensity value lower than the threhsold
value and the second group having intensity value higher than the threshold value.
The output of this process is the binary image"""

img = cv.imread('D:\Learning_ML_Krish\Computer_Vision\images\gradient.png')  

# Let's create a threshold, it gives two values (ret value and threhsold value)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# cv.threshold(src, thresh, maxval, type[threshold type]) 

""" In simple words if the value of the pixel less than the minimum threshval value it considered as 0,
    if the value of the pixel is greater than the minimum threshval value it considered as 255"""

_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) 
 # It gives the inverse of the value if the input value less than threshold then it gives 255,
 #  if the input value is greater than the threshold then it gives 0

_, th3 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)

_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) 
# If the value is less than thresold it don't change, if the pixel value is greater 
# than the threshold the the value remains same. input > 127 then output = 127. 

_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) 
# Whenver you pixel value is less than the threshold value it is set to zero, then pixel value greater than threshold value 
# it remains same.

_, th6 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
# Inverse of the last method

cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)
cv.imshow('th6', th6)


cv.waitKey(0)
cv.destroyAllWindows()
