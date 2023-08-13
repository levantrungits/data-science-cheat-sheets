'''
OpenCV Python Tutorial

Covered in this #8 (Face and Eye Detection - Object Detection):
    1. Haar Cascade explanation
    2. Loading Haar Cascade Classifiers
    3. Face Detection
    4. Eye Detection

'''

import cv2 as cv
import numpy as np

try:
    cap = cv.VideoCapture(0)
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    
    while True:
        ret, frame = cap.read()
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex,ey,ew,eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
            
        cv.imshow('Frame', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()
except Exception as ex:
    print(f"Error: {ex}")
    



