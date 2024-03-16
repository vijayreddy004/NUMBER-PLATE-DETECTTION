import cv2 as cv
import numpy as np
harcascade = cv.CascadeClassifier('har_numberplates.xml')
img = cv.imread('photos/90.jpg')
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
numb = harcascade.detectMultiScale(imgGray,1.2,5)
for x,y,z,h in numb:
    crop = img[y:y+h,x:x+z]
    cv.imshow('number plate',crop)
    cv.rectangle(img,(x,y),(x+z,y+h),(0,255,0),2)
    cv.putText(img,"number plate",(x,y-10),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
cv.imshow('image',img)
cv.waitKey(0)