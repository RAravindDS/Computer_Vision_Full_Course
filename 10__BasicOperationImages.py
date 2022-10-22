import cv2 
import numpy as np 

img = cv2.imread('images\Messi.jpg') 
img2 = cv2.imread('images\opencv-logo.png')  

""" Whenever you have a reading image attirbute or variable, you can use more funcitons lile dtype, shape and size, let's see how to use them """

print(img.shape) # returns a tuple contains number of rows, columns, and channels. 
print(img.size) # returns a total number of pixels in the image.
print(img.dtype) # returns the data type of the image.

""" If you Want to split your images into channels (BGR), you can use the following code"""
# b,g,r = cv2.split(img)

# If you want to merge the channels, you can use the following code!
# img = cv2.merge((b,g,r)) # merge the channels

""" Sometimes you need to work with ROI (Region of Interest) of the image. You can use the following code to do that"""

# ball = img[522:692,  728:810] # Upper Left Corner, Lower Right Corner
# img[322:492, 528:610] = ball # It will copy the ball at indexed place

# It must be in same size 


""" If you want to add  two images with the same size, you can use the following code"""

img = cv2.resize(img, (512, 512)) # Number of rows and number of columns. 
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2)
""" If you want to give weight to seperate image you can use the following code"""
dst = cv2.addWeighted(img, 0.5, img2, 0.5, 0) # 0.5 means 50% of img and 50% of img2
# cvw.addweighed(img1, alpha, img2, beta, gamma) # alpha is the weight of img1, beta is the weight of img2, gamma is the weight of the third image)
# 

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 