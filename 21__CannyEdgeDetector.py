""" 
 It is an edge detection operator that uses multi algorithm to detect wide range of edges in images
    To Execute this, it has 5 types: 
    1. Noise Removal 
    2. Gradient Calculation 
    3. Non-maximum suppression 
    4. Double Threshold
    5. Edge Tracking by Hysteresis

""" 

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png', 0) 


canny = cv2.Canny(img,100,200,) 
# cv2.canny(source, threshold1, threshold2)

titles = ['image', 'canny']
images = [img, canny]



for i in range(len(images)): 
    plt.subplot(2,3, i+1) 
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.tight_layout()
    
plt.show() 
