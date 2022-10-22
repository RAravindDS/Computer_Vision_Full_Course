import cv2 
import numpy as np 

# There are many mouse event available in the OpenCV. To List out all the events use this following code! 

# event = [ i for i in dir(cv2) if 'EVENT' in i]
# print(event)

def click_event(event, x, y, flags, param):
    """ If I Click Left button, it need to show the x and y cordinate """
    if event == cv2.EVENT_LBUTTONDOWN: # for left click buttion down 
        print(x, ' ',y)

        # Then we need to put in the live video: 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2) 
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN: 
        """ I want to print BGR when I write click right button """

        blue = img[y,x, 0] # Channel for blue is 0 
        green = img[y,x,1] # Channel for green is 1
        red = img[y,x,2] # Channel for red is 2

        font = cv2.FONT_HERSHEY_SIMPLEX 
        strXY = str(blue) + ', ' + str(green) + ', ' + str(red) 
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2) 
        cv2.imshow('image', img)



img = cv2.imread('images\ootball.jpg', -1)

cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event) # This function helps to call the click_event function and set the mouse for coordinates.
cv2.waitKey(0)

cv2.destroyAllWindows() 
    


