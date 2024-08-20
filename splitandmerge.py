import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv. imread( '/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/park.jpg')
cv. imshow( 'Park', img)

blank = np.zeros(img. shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)


cv.imshow('Blue_gray',b)
cv.imshow('Green_gray',g)
cv.imshow('Red_gray',r)

print (img.shape)
print (b.shape)
print (g.shape)
print (r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)


cv.waitKey(0)