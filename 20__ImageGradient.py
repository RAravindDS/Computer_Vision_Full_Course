""" Image Gradient is a directional change in an image."""
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\sudoku.png', 0)

""" Lapalacian Gradient Filter """
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize = 3 )# cv2.laplacian(souce, data type, kernel size)
laplacian = np.uint8(np.absolute(laplacian)) # it hep to convert to unit8 (unsigned 8 bit integer) 

""" SobelX"""
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0) # cv2.Sobel(source, data type, x order of derivate x, y order of derivative y )
sobley = cv2.Sobel(img, cv2.CV_64F, 0, 1) # cv2.Sobel(source, data type, x order of derivate x, y order of derivative y ) 

sobelx = np.uint8(np.absolute(sobelx))
sobley = np.uint8(np.absolute(sobley))

sobelcombined = cv2.bitwise_or(sobelx, sobley)
 
titles = ['image','laplacian', 'sobelx', 'sobley', 'sobelcombined']
images = [img, laplacian, sobelx, sobley, sobelcombined]

for i in range(len(images)): 
    plt.subplot(2,3, i+1) 
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.tight_layout()
    
plt.show() 


