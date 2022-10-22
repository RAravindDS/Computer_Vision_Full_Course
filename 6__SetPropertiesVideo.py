import cv2 

b = cv2.VideoCapture(0) # 0 is for default camera on our system. 

print(b.get(cv2.CAP_PROP_FRAME_WIDTH)) # you can also use 3 instead of writing this much lines 
print(b.get(cv2.CAP_PROP_FRAME_HEIGHT)) # you can also use 4 instead of writing this much lines

b.set(cv2.CAP_PROP_FRAME_WIDTH, 3000) # You can set the width of your video 
b.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000) # You can set the height of your video

print(b.get(cv2.CAP_PROP_FRAME_WIDTH)) # you can also use 3 instead of writing this much lines 
print(b.get(cv2.CAP_PROP_FRAME_HEIGHT))

while b.isOpened(): 
    ret, frame = b.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX

     
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 

    else: 
        break 

b.release()
cv2.destroyAllWindows()
