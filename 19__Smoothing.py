"""Smoothing or blurring is the process of reducing the noise in an image, 
   * To smooth, In cv it has more fiter methods in it (homogenous, gaussian, median, bilateral)
   1. Homogenerous filter
   * It is a simple filter, In each output pixel is mean of it's kernel neigbhors. 
   * All pixel contribute it's equal weight, that's why they are called homogenous filter.
    """

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\saltandpepper.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Becuaes matplotlib reads image in RGB format 



kernel = np.ones((5,5), np.float32)/25 # Becuse kernel is 5/5 and we want to divide by 25 

dst = cv2.filter2D(img,-1, kernel) # -1 means depth of the image (Homogenous filter)
# cv2.filter(source, desire depth of image, kernel)

""" LPH (Low pass filter) helps to removing noises, blurring  the images. 
    HPH (high pass filter) helps to removing the edges of the images."""

# First algorithm
blur = cv2.blur(img, (5,5))
# cv2.blur(source, (kernel size))

# gaussian filter algorithm
""" Gaussian filter is nothing but usign differne weight kerenl, in both x and y direction. """

gblur = cv2.GaussianBlur(img, (5,5), 0)
#cv2.GaussianBlur(source, (kernel size), sigmaX(optional))

# median filter algorithm
""" Median filter is something that replaces the each pixel value  with the median of it's neighboring pixels 
This is dealing with salt and pepper noise. """ 
median = cv2.medianBlur(img, 5)
#cv2.medianblue(source, kernelsize(it must be odd size, expect 1 if you give 1 it shows the orginal image))


# Bilateral filter algorithm
""" Bilateral filter is a combination of median and gaussian filter, if you want a sharp edge you can use this"""

bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75)
#bilateralfilter = cv2.bilateralFilter(source, kernelsize, sigmaColor, sigmaSpace) # use lena image 
titles = ['image', '2D Convolution', 'blur', 'Gaussian blur', 'median', 'Bilateral Filter']
image = [img, dst, blur, gblur, median, bilateralfilter] 

for i in range(len(image)): 
    plt.subplot(2, 3, i +1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])  # title is just to show the name of the image

plt.tight_layout()
plt.show() 
