import cv2 
import datetime 



cap = cv2.VideoCapture(0)

cap.set(3, 1500) # set width
cap.set(4, 1500) # set height 

while cap.isOpened(): 
    ret, frame = cap.read()

    if ret == True:
        

        # I want to display the height and width in my live video.So, I can use the following code! 

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame,datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA) 

        
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else: 
        break 

cap.release()
cv2.destroyAllWindows() 