""" * Morphological Operations are simple operations based on the shape of the image.
    * It is normally performed in binary images. 
    * Morphological operations are used to perform image processing on binary images.
    * Two things requires to dot the morphological operations: 1) Orginal image 2) Structuring element or Kernel"""

import cv2 

import matplotlib.pyplot as plt 
import numpy as np 

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\smarties.png', 0) 


_, mask = cv2.threshold(img, 220, 225, cv2.THRESH_BINARY_INV)

# 1. Morphological operations (dialation) 
dilation = cv2.dilate(mask, kernel = np.ones((2,2), np.uint8), iterations= 3)
""" Kernel is normally square or shape, which we want to apply in image"""

# 2. Morphological operations (erosion)
erosion = cv2.erode(mask, kernel = np.ones((5,5), np.uint8), iterations= 3) 

# 3. Morphological operations (opening) | Both the erosion(first) and dilation(second) preforms here 
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel = np.ones((5,5), np.uint8), iterations= 3) 

# 4. Morhological operations (closing) | Both the dilation(first) and erosion(second) preforms here 
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel = np.ones((5,5), np.uint8), iterations= 1)

# 5. Morphological operations (gradient) | It is the difference between dilation and erosion
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel = np.ones((5,5), np.uint8), iterations= 1)

# 6. Morphological operations (tophat) | It is the difference between input image and opening of the image  
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel = np.ones((5,5), np.uint8), iterations= 1)

# more number of techniques available in opencv Just explore those things. 

title = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
image = [img, mask, dilation, erosion, opening, closing, gradient, tophat]

""" Whenever you are doing thresoling try to make the picture in gray scale """

for i in range(len(image)): 
    plt.subplot(3, 3, i +1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
plt.tight_layout()
plt.show()
