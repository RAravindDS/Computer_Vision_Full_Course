""" 
It has three steps to determine the corners in the image.
1. Determines which window produce very large variations intensity when moved in both x, y directions. 
2. With each window found, a R score is computed. 
3. After applying a threshold to this score, important corners are selected. 

What is window? 
- Windows is just corner and you will find the intesity and variation moving in both x, y directions.

1. E(x,v) = w(x,y) [I(x+u, y+v) - I(x-u, y-v)] / (2u + 1)^2 - summation 
2. R = det(M) - k(trace(    M   ))^2
"""

import numpy as np 
import cv2 

img = cv2.imread('D:\\Learning_ML_Krish\\Computer_Vision\\images\\chessboard.png')
cv2.imshow('image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

gray = np.float32(gray) # harris corner takes the image in float format, so we are converting it . 
dst = cv2.cornerHarris(gray, 2, 3, 0.04) # dst is the output of the function.
# (image, blocksize(window), ksize(size of the kernel), k(parameter))

""" 
Block size - It is the size of the neighbour hood consider for corner detection. 
ksize - aperture parameter for sobel derivative used. 
k - harris parameter equation.
"""
dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255] # reverting back to the orignal image.
cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()