import cv2 as cv 
import numpy as np

blank = np. zeros ( (500,500,3), dtype='uint8')
# cv. imshow( 'Blank', blank)

# blank[200:300 , 300:400] = 0,255,0
# cv. imshow( 'Green', blank)

# cv. rectangle(blank, (0,0), (250,500), (0,255, 0), thickness= 20)  #for filling rectangle use thickness = cv.FILLED or -1
# cv. imshow( 'Rectangle', blank)

# #Draw a rectangle
# cv. rectangle(blank, (0,0), (blank. shape [1]//2, blank. shape [0] //2), (0,255, 0) , thickness=-1)
# cv. imshow( 'Rectangle', blank)
 
# #Draw a circle
# cv. circle(blank, (blank. shape[1]//2, blank.shape[0]//2), 40, (0,0,255) ,thickness = -1 )
# cv. imshow( 'Circle', blank)

# # 4. Draw a line
# cv. line (blank, (0,0), (blank. shape[1]//2, blank. shape [0]//2), (255,255,255) , thickness=3)
# cv. imshow('Line', blank)


#write text on the image
cv. putText(blank, 'Hello my name is Paarth', (0,225), cv. FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) 
cv. imshow('Text', blank)

# img = cv. imread ('/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/cat.jpg')
# cv. imshow( 'Cat', img)

cv. waitKey (0)