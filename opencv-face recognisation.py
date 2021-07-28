#todo: foor single img
#/*import cv2
# face_cas=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cap=cv2.VideoCapture(0)
# img=cv2.imread('face.jpg')
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cas.detectMultiScale(gray,1.1,4)
# for (x,y,w,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

# cv2.imshow('img', img)
# cv2.waitKey(0)*/




import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
#img = cv2.imread('test.png')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
