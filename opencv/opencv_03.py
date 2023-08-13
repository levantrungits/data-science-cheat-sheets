'''
OpenCV Python Tutorial

Covered in this #3 (Cameras and VideoCapture):
    1. Displaying video capture device
    2. Mirroring video multiple times

'''

import cv2 as cv
import numpy as np

try:
    cap = cv.VideoCapture(0) # number of cameras
    
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))
        
        image = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv.resize(frame, (0,0), fx=0.5, fy=0.5)
        image[:height//2, :width//2] = cv.rotate(smaller_frame, cv.ROTATE_180) # top-left
        image[height//2:, :width//2] = smaller_frame # bottom-left
        image[:height//2, width//2:] = cv.rotate(smaller_frame, cv.ROTATE_180) # top-right
        image[height//2:, width//2:] = smaller_frame # bottom-right
    
        cv.imshow('frame', image)
        
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    
except Exception as ex:
    print(f"Error: {ex}")
    
cv.destroyAllWindows()

