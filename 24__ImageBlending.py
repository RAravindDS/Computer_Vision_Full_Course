import cv2 
import numpy as np 
apple = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\pple.jpg')
orange = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\orange.jpg')

print(apple.shape)
print(orange.shape)

# I want to blend half of the orange to the apple 
apple_orange = np.hstack((apple[:, :256], orange[:, 256:])) # It will stack the images side by side
print(apple_orange.shape)

""" In order to blend the Image you need to follow 5 steps: 
    1. Load the two images of apple and orange. 
    2. Find the Gaussian Pyramid for both the images.
    3. From Gaussian Pyramid, find their laplacian pyramid. 
    4. Now join the left half of the apple and right half of the orange level of laplacian pyramid. 
    5. Finally from the joint image pyramids, reconstruct the original image. 
"""
# step2 : Find the Gaussian Pyramid for both the images. 
apple_copy = apple.copy()
orange_copy = orange.copy() 

gp_apple = [apple_copy] 
gp_orange = [orange_copy] # to find the laplacia pyramid we need to use the copy of the image

for i in range(6): 
    apple_copy = cv2.pyrDown(apple_copy) 
    gp_apple.append(apple_copy)

    orange_copy = cv2.pyrDown(orange_copy)  
    gp_orange.append(orange_copy) 

# step3 : From Gaussian Pyramid, find their laplacian pyramid. 
apple_copy = gp_apple[5] 
lp_apple = [apple_copy]
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5,0,-1): 
    gaussian_extended = cv2.pyrUp(gp_apple[i]) 
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian) 

    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian) 

# step 4: Now join the left half of the apple and right half of the orange level of laplacian pyramid. 
apple_orange_pyramid = [] 
n = 0 
for apple_lap, orange_lap in zip(lp_apple, lp_orange): 
    n += 1 
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian) 

# step5: Reconstruct the image. 
apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1,6): 
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct )
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)   

cv2.imshow('apple', apple)
cv2.imshow('apple_orange', apple_orange)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)
cv2.imshow('orange', orange)

cv2.waitKey(0)
cv2.destroyAllWindows() 
