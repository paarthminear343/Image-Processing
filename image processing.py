import cv2 as cv



img=cv. imread ('/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/cat.jpg')
cv. imshow( 'Cat', img)
cv. waitKey (0)
# import cv2 as cv

# img = cv.imread('/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Photos/cat.jpg')

# cv.imshow('Cat', img)

# Keep the window open until 'd' is pressed
# while True:
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
 
# cv.destroyAllWindows()


# img=cv. imread ('Photos/cat_large.jpg')
# cv. imshow( 'Cat_large', img)
# cv. waitKey (0)


#READING VIDEOS

capture = cv.VideoCapture('/Users/paarthminear/Downloads/PM/Code/VS code/image processing/Videos/dog.mp4')
while True:
    isTrue , frame = capture.read()
    cv. imshow( 'Video', frame)
    if cv.waitKey (20) & 0xFF==ord('d'):
        break
capture. release
cv. destroyAllWindows