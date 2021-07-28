# harris corner detection 
# import numpy as np
# import cv2 

# img = cv2.imread('chessboard.png')

# cv2.imshow('img', img)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray=np.float32(gray)

# dist=cv2.cornerHarris(gray, 2,3, 0.04)

# dist=cv2.dilate(dist,None)

# img[dist>0.01* dist.max()]=(0,255,0)
# cv2.imshow('dist', img)

# if cv2.waitKey(0) & 0xff == ord('q'):
#     cv2.destroyAllWindows()


# shi tomasi corner detector(as comapred this is better)
import numpy as np
import cv2 as cv

img = cv.imread('pic1.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, [255, 255, 0], -1)

cv.imshow('Shi-Tomasi Corner Detector', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()