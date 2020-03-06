import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img = cv2.imread("E:\\USER DATA\\Desktop\\Training Data Set\\Archies\\1.jpg",0)
edge = cv2.Canny(img, 50, 200) 



d = pytesseract.image_to_data(edge, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
    edge = cv2.rectangle(edge, (x, y), (x + w, y + h), (130, 20, 243), 2)

cv2.imshow('tess',edge)
cv2.waitKey(0)
extracted_text = pytesseract.image_to_string(img, lang = 'eng')


print(extracted_text)


receipt_ocr = {}
splits = extracted_text.splitlines()
print(splits)
restaurant_name = splits[2]
import re
# regex for date. The pattern in the receipt is in 30.07.2007 in DD:MM:YYYY

date_pattern = '24-10-2019'
date = re.search(date_pattern, extracted_text).group()
receipt_ocr['date'] = date
print(restaurant_name,date)



totals = []
tax = []
for i in splits:
    if "Total" in i:
        totals.append(i)
    if "Tax" in i:
        if "$" in i:
            tax.append(i)

subtotal_dict = {}
total_dict = {}
tax_dict={} 

for i in totals:
    if "Sub Total" in i:
        sub_temp = i.split()
        subtotal_dict[str(sub_temp[0] + " " + sub_temp[1])] = sub_temp[2]

        
tax_temp = tax[0].split()       
tax_dict[str(tax_temp[0] + " " + tax_temp[1])] = tax_temp[2]

total_temp = totals[-1].split()
total_dict[str(total_temp[0])] = total_temp[1]



print("Restuarant_name:" + " " + restaurant_name)
print("Date:" + " " + date)
print(subtotal_dict)
print(tax_dict)
print(total_dict)


bill_df = pd.DataFrame({"Restaurant Name" : [restaurant_name], "Date" : [date], "Sub_Total" : subtotal_dict.values(),
                       "Tax" : tax_dict.values(), "Total" : total_dict.values()})


print(bill_df)
