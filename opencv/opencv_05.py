'''
OpenCV Python Tutorial

Covered in this #5 (Colors and Color Detection):
    1. HSV Color
    2. Masks

'''

import cv2 as cv
import numpy as np

try:
    cap = cv.VideoCapture(0) # number of cameras
    
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))
        
        '''
            BGR_color = np.array([[[255, 0, 0]]])
            cv.cvtColor(BGR_color, cv.COLOR_BGR2HSV)
            print(cv.cvtColor(BGR_color, cv.COLOR_BGR2HSV))
        '''
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])
        
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        
        result = cv.bitwise_and(frame, frame, mask=mask)
        '''
        1 1 = 1
        0 1 = 0
        1 0 = 0
        0 0 = 0
        '''
                
        cv.imshow('frame', result)
        cv.imshow('mask', mask)
        
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    
except Exception as ex:
    print(f"Error: {ex}")
    
cv.destroyAllWindows()

