import cv2 
import numpy as np 
import matplotlib.pyplot as plt

img = np.zeros((200,200), np.uint8) 
cv2.rectangle(img, (0,100), (200,200), 255, -1) 
cv2.rectangle(img, (0,50), (100,100), 127, -1) 

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png', 1)
b, g, r = cv2.split(img)

""" Finding Histogram of an Image"""
plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.grid()
plt.tight_layout()
plt.show()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
