import cv2 

""" To save the video, we need to use the VideoWriter class """

cap = cv2.VideoCapture(0);
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (640, 480)) 

# cv2.VideoWriter('Name of our Output file', Fourcc code, fps, (width, height)) 

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('frame', frame)
        out.write(frame) # it helps to write the frame to the video file

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
    else: 
        break 

cap.release()
out.release()
cv2.destroyAllWindows() 
