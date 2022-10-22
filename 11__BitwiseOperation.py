import cv2
import numpy as np 

img1 = np.zeros((183,275, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img3 = cv2.imread('images/HBHW.png')

cv2.imshow('img1', img3)
# cv2.imshow('img2', img2)



# bitAnd = cv2.bitwise_and(img3, img1)
""" Bit wise operations, if the both are having 1 then only the result is 1 else 0 """

# bitOr = cv2.bitwise_or(img3, img1)
""" Bit Or operations, if 1 input is 1 the output is 1 else 0 """

# bitxor = cv2.bitwise_xor(img3, img1)
""" If both the inputs are 0 or 1 then we will get the 0 otherwise 1"""

bitnot = cv2.bitwise_not(img3)

""" It just a opposite of input if input 0 the output is 1"""
cv2.imshow('bitAnd', bitnot)
cv2.waitKey(0)
cv2.destroyAllWindows() 
 