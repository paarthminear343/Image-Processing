import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv. imread( '/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/cats.jpg')
cv. imshow( 'Cats', img)

average = cv. blur (img, (7,7))
cv. imshow( 'Average Blur', average)

#gaussian blur is more natural than average blur

gau = cv.GaussianBlur(img , (7,7) , 0)
cv.imshow('Gaussian Blur', gau)

# median blur used for reducing noise and making smooth
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# bilateral blur
bilateral = cv.bilateralFilter(img, 7 , 50, 50)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)