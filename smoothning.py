import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv. imread( '/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/flower.jpeg')
cv. imshow( 'Flower', img)

average = cv. blur (img, (10,10))
cv. imshow( 'Average Blur', average)

cv.waitKey(0)