import numpy as np
import cv2
import math
import os
from scipy import ndimage


def check_image(impath):
    print(impath)
    dir, fname = impath.split('/')
    img = cv2.imread(impath,0)
    # cv2.imshow("chutiyap",img)
    # cv2.waitKey(0)
    (h, w) = img.shape[:2]
    if w>h:
        dst = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        # cv2.imshow("chutiyap",dst)    
        # cv2.waitKey(0)    
        cv2.imwrite(dir + os.sep + 'rot90_'+fname,dst)

lis = os.listdir('images')
for images in lis:
    impath = 'images/'+images
    check_image(impath)