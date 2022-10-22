""" 
 It is an edge detection operator that uses multi algorithm to detect wide range of edges in images
    To Execute this, it has 5 types: 
    1. Noise Removal 
    2. Gradient Calculation 
    3. Non-maximum suppression 
    4. Double Threshold
    5. Edge Tracking by Hysteresis

""" 

from re import S
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png', cv2.Conv) 
cv2.namedWindow('bar') 
def nothing(x):
    print(x)

cv2.createTrackbar('Value A', 'bar', 0, 255, nothing)
cv2.createTrackbar('Value B', 'bar', 0, 255, nothing) 

while True: 
    ta = cv2.getTrackbarPos('Value A', 'bar') 
    tb = cv2.getTrackbarPos('Value B', 'bar') 
    can = cv2.Canny(img, ta, tb)
    cv2.imshow('bar', can)
    k = cv2.waitKey(0) & 0xFF
    if (k == 27): 
        break


 
