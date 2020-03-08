import cv2
import numpy as np
import pytesseract
from pytesseract import Output

def ocr(imgpath):
    '''
    input : path to the img file
    output: text
    '''
    img = cv2.imread(imgpath,0)
    (h, w) = img.shape[:2]
    if w>h:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 
    edge = cv2.Canny(img, 50, 200) 
    d = pytesseract.image_to_data(edge, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
        edge = cv2.rectangle(edge, (x, y), (x + w, y + h), (130, 20, 243), 2)
    extracted_text = pytesseract.image_to_string(img, lang = 'eng')
    # print(extracted_text)
    return extracted_text, extracted_text.splitlines()
