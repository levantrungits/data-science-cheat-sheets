'''
OpenCV Python Tutorial

Covered in this #4 (Drawing: Lines, Images, Circles, Text):
    1. Drawing Lines
    2. Drawing Rectangles
    3. Drawing Text

'''

import cv2 as cv

try:
    cap = cv.VideoCapture(0) # number of cameras
    
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))
        
        img = cv.line(frame, (0,0), (width, height), (255, 0, 0), 10)
        img = cv.line(img, (0,height), (width, 0), (0, 255, 0), 10)
        img = cv.rectangle(img, (100,100), (200,200), (128, 128, 128), 5)
        img = cv.circle(img, (300,300), 60, (0, 0, 255), -1)
        font = cv.FONT_HERSHEY_SIMPLEX
        img = cv.putText(img, 'levantrungits@outlook.com is Great!', (10, height-10), font, 3, (0, 0, 0), cv.LINE_8)
    
        cv.imshow('frame', img)
        
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    
except Exception as ex:
    print(f"Error: {ex}")
    
cv.destroyAllWindows()

