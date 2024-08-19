import cv2 as cv
import numpy as np

img = cv. imread( '/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/group 1.jpg')

cv. imshow( 'Group photo', img)


# Translation
def translate(img, x, y):
    transMat = np. float32([[1,0, x], [0,1, y] ])
    dimensions = (img. shape [1], img. shape [0])
    return cv.warpAffine(img, transMat, dimensions)  

#=X==> Left
#=Y==> Up
# x -→> Right 
# # y --› Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

#rotation
def rotate(img, angle, rotPoint=None) :
    (height, width) = img. shape[: 2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv. imshow( 'Rotated', rotated)

rotated2 = rotate (img, 90)
cv.imshow('Rotated2', rotated2) 

# Flipping
flip= cv. flip (img, -1)  #0 for vertical flip , 1 for horizontal flip , -1 for both
cv. imshow( 'Flip', flip)

cv. waitKey (0)