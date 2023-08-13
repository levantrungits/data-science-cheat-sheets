'''
OpenCV Python Tutorial

Covered in this #7 (Template Matching - Object Detection):
    1. Loading Template & Base Image
    2. Template Matching Methods
    3. Theory Behind Template Matching

'''

import cv2 as cv
import numpy as np

try:
    img = cv.imread('../assets/images/soccer_practice.jpg', 0)
    template = cv.imread('../assets/images/shoe.PNG', 0)
    h, w = template.shape
    
    methods = [
        cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
        cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED
    ]
    
    for method in methods:
        img2 = img.copy()
        
        # (W - w + 1, H - h + 1)
        result = cv.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(f"{min_loc} === {max_loc} ")
        
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc
        
        bottom_right = (location[0] + w, location[1] + h)
        
        cv.rectangle(img2, location, bottom_right, 255, 5)
        
        cv.imshow('Match', img2)
        cv.waitKey(0)
        cv.destroyAllWindows()
    
except Exception as ex:
    print(f"Error: {ex}")
    



