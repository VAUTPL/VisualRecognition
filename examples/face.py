import numpy as np
import cv2
import visual_recognition_v3
import time

face_cascade = cv2.CascadeClassifier('../resources/cascades/haarcascade_frontalface_default.xml')

def ejecutar():
    cap = cv2.VideoCapture(0)
    foto='../resources/ingreso2.jpg'

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        

        for (x,y,w,h) in faces:
            #print('Imagen reconocida')
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),0)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            height, width = img.shape[:2]
            res = cv2.resize(roi_color,(width, height), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(foto, res)
            visual_recognition_v3.visual_recognition(foto)
            break
ejecutar()

