""" We used images with constant size, Using image pyrmaid we can create image of different resoulion, then we search for the best match

    * Pyramid is a multi scale signal representation. It is two pyramids
    1. Gaussian (Repeat filtering and sub sampling of image)
    2. Laplacian  """

import cv2 
import numpy as np 
import matplotlib.pyplot as plt  

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png') 

# lr = cv2.pyrDown(img)
# hr = cv2.pyrUp(lr) 




# cv2.imshow('orginal image', img)
# cv2.imshow('lower resolution', lr) #(1/4 image)
# cv2.imshow('higher resolution', hr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

""" If you want to use multiple resolution you can use this code"""

# layer = img.copy()
# gp = [layer]

# for i in range(6): 
#     layer = cv2.pyrDown(layer)
#     gp.append(layer)
#     cv2.imshow(str(i), layer)

# cv2.imshow('orginal image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


""" Their is no function to create laplacian pyramid, so we will use the code below
    A level in the laplacian pyramid is formed by the difference between the level in the gaussina pyramid and the expanded version of the upper gaussian pyramid"""



# layer = img.copy()
# gp = [layer]

# for i in range(6): 
#     layer = cv2.pyrDown(layer)
#     gp.append(layer)
#     #cv2.imshow(str(i), layer)

# layer = gp[5]
# cv2.imshow('upperlevel in gaussian pyramid', layer) 

# lp = [layer]

# for i in range(5,0, -1):
#     gaussian_estended = cv2.pyrUp(gp[i])  # It gives the extended version of the gaussian pyramid
#     laplacian = cv2.subtract(gp[i-1], gaussian_estended) # It gives the difference between the gaussian pyramid and the extended version of the gaussian pyramid

#     cv2.imshow(str(i), laplacian)



# cv2.imshow('orginal image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


