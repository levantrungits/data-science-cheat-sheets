'''
OpenCV Python Tutorial

Covered in this #1 (Introduction & Images)
    1. Installation & Setup 
    2. Loading an Image
    3. Displaying an Image
    4. Resizing an Image
    5. Rotating an Image
'''

import cv2

try:
    ''' 
    -1: cv2.IMREAD_COLOR
    0: cv2.IMREAD_GRAYSCALE
    1: cv2.IMREAD_UNCHANGED
    '''
    img = cv2.imread('../assets/images/Me_2023-07-24_DL.png', 1)
    
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite('../assets/images/NEW_Me_2023-07-24_DL.png', img)
    
    cv2.imshow('levantrungits', img)
    cv2.waitKey(0) # wait for a keyboard input
    
except Exception as ex:
    # Need lib: opencv-python-headless-4.8.0.76
    # Error: OpenCV(4.8.0) window.cpp:971: error: (-215:Assertion failed) 
    #   size.width>0 && size.height>0 in function 'imshow'
    print(f"Error: {ex}")
    
cv2.destroyAllWindows()
