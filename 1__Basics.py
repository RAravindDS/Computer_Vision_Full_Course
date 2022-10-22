import cv2

# You can refer this notebook for basics https://colab.research.google.com/drive/1yjBn_1z8zD4T6wU0OjoQ9-QzGUR6b8uV

print('True')

b = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png', 1)
# 1 is for color image, 0 is for grayscale image, -1 is for unchanged image (default) 

cv2.imshow('image', b)

# It don't show longer so we can use waitkey 

cv2.waitKey(0) # 0 means infinite time, if you want to show it for 1 sec then you can use 1000, if you want to show it for 2 sec then you can use 2000


# if you want to close the window then you can use this 
cv2.destroyAllWindows()


# If you want to write the image you can use this 

""" cv2.imwrite(filename, image[, params])"""

cv2.imwrite('lena.copy.png', b) # see the folder, we have a image called lena.copy.png and b is the image we want to write in it

# let;s go deeper 

b = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png', 1)
cv2.imshow('image', b)

k = cv2.waitKey(0) & 0xFF # 0xFF is for masking the value especially for windows 64 bit

if k == 27: # 27 is the ASCII code for ESC key
    cv2.destroyAllWindows() 

elif k == ord('s'):
    cv2.imwrite('lena.copy.png', b)
    cv2.destroyAllWindows() 

# If you want to get more images, you can use this link 
#https://github.com/opencv/opencv/tree/master/samples/data