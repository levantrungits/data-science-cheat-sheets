'''
OpenCV Python Tutorial

Covered in this #6 (Corner Detection):
    1. Corner detection
    2. Drawing corners
    3. Drawing lines between corners

'''

import cv2 as cv
import numpy as np

try:
    img = cv.imread('../assets/images/chessboard.png')
    img = cv.resize(img, (0,0), fx=0.5, fy=0.5)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    '''
        (source image, number of corners, minimum quality, minimum EUCLIDEAN distance)
        (x1, y1) (x2, y2)
        sqrt((x2-x1)^2 + (y2-y1)^2)
    '''
    corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10) 
    corners = np.int64(corners)
    
    for corner in corners:
        x, y = corner.ravel()
        cv.circle(img, (x,y), 5, (255,0,0), -1)
        
    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            corner1 = tuple(corners[i][0])
            corner2 = tuple(corners[j][0])
            color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
            cv.line(img, corner1, corner2, color, 1)
    
    cv.imshow('Frame', img)
    cv.waitKey(0)
    
except Exception as ex:
    print(f"Error: {ex}")
    
cv.destroyAllWindows()


