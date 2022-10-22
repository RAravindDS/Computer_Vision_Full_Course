import cv2 


cap = cv2.VideoCapture(0) # 0 is for default camera, 1 is for external camera if 0 doesn't work then try -1 

# In order to capture the frames, we are going to use the while loop 

while True: 

    """"""
    ret, frame = cap.read() # ret is for return value (like if capture, it returns Ture or False), frame is for frames 

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # cv2.COLOR_BGR2GRAY is for converting the color image to grayscale image 
    #cv2.imshow('frame', gray) # gray is for grayscale image 

    cv2.imshow('frame', frame) # frame is the name of the window, frame is the image. 

    if cv2.waitKey(1) &  0xFF == ord('q'): # q is for quit, if you press q then it will quit
        break

""" After Reading a Video we need to release, it is a compulsary Method"""

cap.release()
cv2.destroyAllWindows() 



