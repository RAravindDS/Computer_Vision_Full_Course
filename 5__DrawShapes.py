import cv2 


img = cv2.imread('D:\Learning_ML_Krish\Computer_Vision\images\lena.png', -1) 

""" To Draw a Line we need to use the cv2.line() function """

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5) # (image, start point, end point, color, thickness)

# (0, 0) is the Cordinate starting point, (255, 255) is the ending Quardinate point, (255, 0, 0) (B G R) is the color, 5 is the thickness
# If you want to draw a green line, you can use (0, 255, 0), for red line, you can use (0, 0, 255), for blue line, you can use (255, 0, 0) 

""" If you want to specify a separte unique desire color, you can go to web search key 'rgb color picker' and remeber we need to 
specify in the form of BGR (Blue Green Red)  but in online RGB, just change and implement this in code (235, 242, 196) 

Just visit this website https://www.google.com/search?q=rgb+color+picker&oq=rgb+color+picker+&aqs=chrome..69i57j0i512l9.7428j0j7&sourceid=chrome&ie=UTF-8"""
  
# if you want to print arrow, use this code 

#img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)

# If you want to draw a rectangle, use this code 
#img = cv2.rectangle(img, (0, 0), (255, 255), (0, 255, 0), 5) 

# Second argumenti Top left vertex 
# x1,y1 -------- (Top Vertex Cordinate) 
# |            |
# |            | 
# |---------x2,y2( Bottom Vertex Cordinate ) 

# If you give -1 for thickness, it will fill the rectangle 

# To draw a circle 
# img = cv2.circle(img, (255, 255), 100, (0, 0, 255), 3) 
# cv2.cricle(imge, center of the circle, radius of the circle, color, thickness) 


# To put text 
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img, 'My Name is Lisa', (10, 500),font, 4, (0,255,0), 10, cv2.LINE_AA)
# cv2.puttext(imgage, text, (x,y) cordinate of the text, font style, fontsize,color, thickness, line type )



cv2.imshow('image', img)
cv2.waitKey(0) 

cv2.destroyAllWindows()  


