
import numpy as np 
import cv2 

img = cv2.imread('D:\\Learning_ML_Krish\\Computer_Vision\\images\\pic1.png')
cv2.imshow('image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

dst = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10) 
# (image, maxCorners, qualityLevel, minDistance)

corners = np.int0(dst)
for i in corners: 
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()