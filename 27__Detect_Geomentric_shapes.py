import cv2

img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\sop.png', 1)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, thrash = cv2.threshold(imgray, 240, 255, cv2.THRESH_BINARY) 

contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

for contour in contours: 
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True) 
    # cv2.approxPolyDP(curve, epsilon, closed)
    # This method approximates the polygonal curve(s) with the specified precision.
    # It returns the number of vertices in the polygonal curve.
    # epsilon – Parameter specifying the approximation accuracy. This is the maximum distance between the original curve and its approximation.
    # closed – Parameter specifying whether the approximated curve is closed or not.
    # If it is true, the last vertex is added to the beginning of the result.
    # If false, the last vertex is not added.
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 5)
    x = approx.ravel()[0] 
    y = approx.ravel()[1] # ravel is used to flatten the array
    if len(approx) == 3: 
        cv2.putText(img, 'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
    elif len(approx) == 4: 
        x,y ,w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h 
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, 'Square',(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2) 
        else:
            cv2.putText(img, 'Rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
    elif len(approx) == 5: 
        cv2.putText(img, 'Pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
    elif len(approx) == 10: 
        cv2.putText(img, 'Star',(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2) 
    else: 
        cv2.putText(img, 'Circle',(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)

cv2.imshow('image', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()