""" 
The process of locating the object in the moving time of the camera - object Tracking. 
Consider a points, you have given a window, you need to change or move the window where the maximum number of points - mean shift. 
1. We need to pass the inital location of the target object and the histogram back projected image to the mean shift function.
2. Object moves, the histogram back projected images is also moves or updated. 
3. The mean shift fucntion, moves the window to the new location where the maximum number of points.
"""

import cv2 as cv
import cv2
from cv2 import calcHist
from cv2 import NORM_MINMAX
from cv2 import calcBackProject
from cv2 import meanShift
from cv2 import TERM_CRITERIA_COUNT
import numpy as np

cap = cv.VideoCapture(0) 
# 1. Take first frame of the video 
ret, frame = cap.read()
# 2. setup initial location of window
x,y,width,height = 300, 200, 100, 50
track_window = (x,y,width, height)
# 3. set up the ROI for tracking
roi = frame[y:y+height, x:x+width]

hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)) )# for making histogram
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180],[0,180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX )
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
# 4. setup the termination criteria, either 10 iteration or move by atleast 1 pt
while(1): 
    ret, frame = cap.read()
    if ret == True: 
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

        # apply mean shift 
        ret, track_window = cv.meanShift(dst, track_window, term_crit) 
        # 5. Now, we need to draw the rectangle on the image
        x,y,w,h = track_window
        final_image = cv.rectangle(frame, (x,y), (x+w, y+h), 255, 2)
        cv.imshow('final_image', final_image)
        if cv.waitKey(1) & 0xFF == ord('q'): 
            break
    else: 
        break 

cap.release()
cv2.destroyAllWindows()