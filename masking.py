import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv. imread( '/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/cats.jpg')
cv. imshow( 'Group of cats', img)

blank = np. zeros (img.shape [:2], dtype='uint8')
cv.imshow('Blank' , blank)

circle = cv. circle(blank.copy(), (img. shape [1]//2+90, img. shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

rectangle = cv.rectangle (blank.copy() , (30,30), (370,370), 255,-1)
cv.imshow('Rectangle', rectangle)

bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND', bitwise_and)



masked_img = cv.bitwise_and(img , img , mask=bitwise_and)
cv.imshow('Masked Image', masked_img) 

cv.waitKey(0)