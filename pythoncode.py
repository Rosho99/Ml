#install on the local terminal: pip3 install opencv-python
#existing name file test
import cv2 as cv
#img = cv.imread("path/to/image")
img = cv.imread("c:/Users/USER/OneDrive/Desktop/corsopython/test.jpg",0) #0 is black and white
cv.imshow("Display window", img)
k = cv.waitKey(0)
