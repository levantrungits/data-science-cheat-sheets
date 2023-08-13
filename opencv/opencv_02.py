'''
OpenCV Python Tutorial

Covered in this #2 (Image Fundamentals and Manipulation):
    1. Image Representation
    2. Values that Represent our Pixels
    3. Accessing Pixel Values
    4. Changing Pixel Colors
    5. Copying & Pasting Parts of Image

Pixel in Image:
    blue green red
    [0,  0,    0]
    0-255
'''

import cv2 as cv
import random

try:
    img = cv.imread('../assets/images/Me_2023-07-24_DL.png', cv.IMREAD_COLOR) # numpy.ndarray
    print(f"img.shape \n {img.shape}") # (row, column, channels(D))
    print(f"img[0] \n {img[257]}") # row 257
    print(f"img[257][45:400] \n {img[257][45:400]}")
    
    # random and replace Pixels
    for i in range(100):
        for j in range(img.shape[1]):
            img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            
    # copy and replace Pixels
    tag = img[400:700, 600:900]
    img[100:300, 650:950] = tag

    cv.imshow('levantrungits', img)
    cv.waitKey(0)
    
except Exception as ex:
    print(f"Error: {ex}")

cv.destroyAllWindows()