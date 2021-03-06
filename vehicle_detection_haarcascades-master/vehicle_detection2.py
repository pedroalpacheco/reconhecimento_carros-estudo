# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)





cascade_src = 'cars.xml'
#video_src = 'dataset/video1.avi'
video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)


while True:
    ret, img = cap.read()
    if type(img) == type(None):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.09, 1)
    #cars = car_cascade.detectMultiScale(gray, 1.09, 1, minSize=(30, 30))

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h ), (51, 255, 51), 2)
        #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)
        #print(cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2))
        #print(len(cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)))


    
    cv2.imshow('Transito', img)
    
    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()