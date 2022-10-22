import matplotlib.pyplot as plt 


import cv2 
import numpy as np 

""" Matplotlib is widely used in CV to show the graph and images"""

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png')
cv2.imshow('image', img) 
""" Matplotlib shows color formar in RGB but CV shows in BGR"""

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
#plt.xticks([]), plt.yticks([]) # it will hide the x and y axis numbers 
plt.show() 

cv2.waitKey(0)
cv2.destroyAllWindows()

""" If you to show multiple plots in one window, you can use subplot """
img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\gradient.png')

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY) 
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) 
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th6 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Orginal Image', 'Binary', 'Binary Inverse', 'Trunc', 'To Zero', 'To Zero Inverse']  
images = [img, th1, th2, th3, th4, th5, th6]

for i in range(6):
    plt.subplot(2, 3, i +1), plt.imshow(images[i], 'gray')
    plt.title(titles[i]) 

plt.show()

