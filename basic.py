import cv2 as cv

img = cv. imread('/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/group 1.jpg')
cv. imshow( 'Group photo', img)
 
# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow ('Gray', gray)
# cv. imwrite("Group gray scale.png",gray)

#blur
blur = cv. GaussianBlur (img, (3,3), cv.BORDER_DEFAULT)
cv. imshow ('Blur image', blur)

#edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow('Canny', canny)

#dialating the image
dialted = cv.dilate(canny, (3,3) , iterations = 1)
cv.imshow('Dialted', dialted)

# Eroding
eroded = cv. erode(dialted, (7,7), iterations=1)
cv. imshow( 'Eroded', eroded)

# Resize
resized= cv. resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv. imshow ('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv. imshow( 'Cropped', cropped)

cv. waitKey (0)