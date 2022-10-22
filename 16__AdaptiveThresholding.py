import numpy as np 
import cv2  as cv

""" Adaptive Thresholding is a method for caluclating the threshold for a smaller region, It's not global for every pixle but 
it calcualted for every region, Threfore different threshold value for different region.""" 

""" Adaptive Thresholding gives a better results for image where everying elimniation """

img = cv.imread('D:\Learning_ML_Krish\Computer_Vision\images\sudoku.png',0) 

# Thresh binary 
_, th1  = cv.threshold(img,127, 255, cv.THRESH_BINARY )

# adatptive binary 
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) 

# cv.adaptivethreshold(source, maxvalue, adaptive method (mean),threshold type, block size, value of c (constant))  
""" Two types of adaptive method, mean and gaussian c """

th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('image', img)
#cv.imshow('image', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)


cv.waitKey(0)
cv.destroyAllWindows()
