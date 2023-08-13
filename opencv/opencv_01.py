'''
OpenCV Python Tutorial

Covered in this #1 (Introduction & Images)
https://docs.opencv.org/4.8.0/df/d9d/tutorial_py_colorspaces.html 
    1. Installation & Setup 
    2. Loading an Image
    3. Displaying an Image
    4. Resizing an Image
    5. Rotating an Image
'''

import cv2 as cv

try:
    ''' 
    -1: cv2.IMREAD_COLOR
    0: cv2.IMREAD_GRAYSCALE
    1: cv2.IMREAD_UNCHANGED
    '''
    img = cv.imread('../assets/images/Me_2023-07-24_DL.png', cv.IMREAD_GRAYSCALE)  # numpy.ndarray
    
    img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
    img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
    cv.imwrite('../assets/images/NEW_Me_2023-07-24_DL.png', img)
    
    cv.imshow('levantrungits', img)
    cv.waitKey(0) # wait for a keyboard input
    
except Exception as ex:
    # Need lib: opencv-python-headless-4.8.0.76
    # Error: OpenCV(4.8.0) window.cpp:971: error: (-215:Assertion failed) 
    #   size.width>0 && size.height>0 in function 'imshow'
    print(f"Error: {ex}")
    
cv.destroyAllWindows()
