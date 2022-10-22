""" 
Background Subraction is technique to generate the fore ground mask which is also known as binary image containing the pixel belonging to the the moving 
object of the seen, when this images are captured as a static camera. 

Foreground mask performing the subtraction in the current frame and the background frame. 
"""

import cv2 as cv
import cv2
import numpy as np 

cap = cv.VideoCapture('D:\\Learning_ML_Krish\\Computer_Vision\\Vidoes\\test.avi') 

fgbg = cv2.createBackgroundSubtractorMOG2()
# we have more algo like, bgsegm.createBackgroundSubtractorGMG(), bgsegm.createBackgroundSubtractorCNT(), bgsegm.createBackgroundSubtractorLSBP() and more..  


while cap.isOpened(): 
    ret, frame = cap.read() 
    if frame is None: 
        break 
    fgmask = fgbg.apply(frame) # getting the foreground mask

    cv.imshow('frame', frame)
    cv.imshow('FG ', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()
