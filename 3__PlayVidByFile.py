import cv2 

b = cv2.VideoCapture(0) # you can give your path, it will read here 

""" some time your path is wrong, to find is there any video you can use this"""

while (b.isOpened()): # If file path is wrong then it will return False or vise versa 
    ret, frame = b.read()

    # if is opened gives you false, you can open your caputred video by using this 

    print(b.get(cv2.CAP_PROP_FRAME_WIDTH)) # it will give you the width of the video (This is prop ID  )
    print(b.get(cv2.CAP_PROP_FRAME_HEIGHT)) # it will give you the height of the video

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break






