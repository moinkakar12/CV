#(a) Write a code to apply the following kernels. [1,1,1],[1,1,1],[1,1,1]
         

import cv2
import numpy as np

img = cv2.imread("Lenna.png",0)


kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9

box_filter = cv2.filter2D(img,-1,kernel)


cv2.imshow("Box", box_filter)
cv2.imshow("Orig_Image", img)

cv2.waitKey(0)


#(b) [-1, 0 , 1]

import cv2 
import numpy as np

img = cv2.imread("flower.jpg",0)

cv2.imshow("Image", img)

kernel = np.array([[-1,0,1]])

cent_diff = cv2.filter2D(img, -1, kernel)

cv2.imshow("Edge", cent_diff)

cv2.waitKey(0)



#(c) [-1,0,1],[-1,0,1],[-1,0,1]

import cv2
import numpy as np

img = cv2.imread("flower.jpg",0)

cv2.imshow("Image", img)
edge = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

edges = cv2.filter2D(img, -1, edge)

cv2.imshow("Y_Axis Edges", edges)

cv2.waitKey(0) 

#(2) Define a function that takes an image and kernel as an argument and return the resultant image.

import cv2
import numpy as np

def img_filter(image='moin.jpg', kernel=np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])):
    image = cv2.imread(image, 0)
    result = cv2.filter2D(image, -1, kernel)
    return result

result = img_filter()
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Q3(a) Derivate in x and y.

import cv2
import numpy as np

img = cv2.imread("albert.jpg")
#blur = cv2.GaussianBlur(img,(3,3),-1)

x = np.array([1,-1])
y = np.array([[-1],[1]])
   
deriv_x = cv2.filter2D(img,-1,x)
deriv_y = cv2.filter2D(img,-1,y)

cv2.imshow("Original_img", img)
cv2.imshow("DX", deriv_x)
cv2.imshow("DY", deriv_y)

cv2.waitKey(0)


#Q3(b) Find the Magnitude M. 

import cv2
import numpy as np

img = cv2.imread("Lenna.png",0)

blur = cv2.GaussianBlur(img,(3,3),0)

sobel_x = cv2.Sobel(blur, cv2.CV_64F,1,0,1)
sobel_y = cv2.Sobel(blur, cv2.CV_64F,0,1,1)

mag = np.sqrt(sobel_x**2 + sobel_y**2)
mag = np.uint8(mag)

cv2.imshow("Image", img)
cv2.imshow("Gradient_Magnitude", mag)

cv2.waitKey(0)

#Q3(c) Threshold the image.

import cv2

img = cv2.imread('flower.jpg',0)
gaussian = cv2.GaussianBlur(img,(3,3),0)

dx = cv2.Sobel(gaussian, cv2.CV_64F,1,0,1)
dy = cv2.Sobel(gaussian, cv2.CV_64F,0,1,1)
mag = cv2.magnitude(dx,dy)

ret, threshold = cv2.threshold(mag, 50, 255, cv2.THRESH_BINARY)
 
cv2.imshow("original",img)
cv2.imshow("Threshold",threshold)

cv2.waitKey(0)


