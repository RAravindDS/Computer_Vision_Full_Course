import cv2 
# img = cv2.imread('D:\\Learning_ML_Krish\\Computer_Vision\\images\\lena.png')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # becase cascade works well on gray scale images.
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# # (Image, scalefactor,minNeighbours)
# """ 
# scale Factor - How much the image size is reduced at each image scale. 
# minNeighbors - How many neighbors each candidate rectangle should have to retain it.
# The output of this will be a vector of rectangle. 
# """
# for (x,y,w,h) in faces: 
#     cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3) 

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#______________________________________ Video Capture _________________________________________

cap = cv2.VideoCapture(0)
while cap.isOpened(): 
    _, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # becase cascade works well on gray scale images.  

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces: 
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3) 

    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
cap.release()
cv2.destroyAllWindows()


















""" If you want to find more model, you can find in this link: 
https://github.com/opencv/opencv/tree/master/data/haarcascades

"""

