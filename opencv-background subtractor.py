import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))#3
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()#1(old method not working)
#fgbg = cv.bgsegm.BackgroundSubtractorGMG()#3(not good)
# fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)#2(new method)
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)#4
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)#3

    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == ord('q') or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()