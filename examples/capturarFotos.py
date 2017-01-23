import numpy as np
import cv2
import time

#python capturafotos.py

face_cascade = cv2.CascadeClassifier('../resources/cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
foto='../resources/'
i=1
nombreIng = raw_input('ingrese el nombre: ')
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        height, width = img.shape[:2]
        res = cv2.resize(roi_color,(width, height), interpolation = cv2.INTER_CUBIC)
        time.sleep(2)
        cv2.imwrite((foto+nombreIng+str(i)+'.jpg'), res)
        print('foto'+str(i))
        i=i+1
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if i == 51:
        break
cap.release()
cv2.destroyAllWindows()