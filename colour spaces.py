import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv. imread( '/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/sceneray.jpg')
cv. imshow( 'Group photo', img)

hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
cv.imshow('HSV' , hsv)

lab = cv.cvtColor (img , cv.COLOR_BGR2LAB)
cv.imshow('LAB' , lab) 
 


rgb = cv.cvtColor (img , cv.COLOR_BGR2RGB)
cv.imshow('RGB' , rgb) 

# plt.imshow(rgb )
# plt.show()

hsv_bgr = cv. cvtColor (hsv, cv. COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

lab_bgr = cv. cvtColor (lab, cv. COLOR_LAB2BGR)
cv. imshow(' LAB --> BGR', lab_bgr)



cv. waitKey (0)