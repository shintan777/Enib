import sys
from model.ocr import ocr
from model.extract  import *
import pytesseract
import time

## if using windows paste the file location of tesseract.exe here, else comment below line 
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def run(imgpath):
    #ocr
    text, lines = ocr(imgpath)
    json = {}

    date = get_date(lines)
    json['date'] = date['date']

    time = get_time(lines)
    json['time'] = time['time']
    
    invoice_no = get_invoice_no(lines)
    json['Invoice No'] = invoice_no['invoice_no']

    address = get_address(lines)
    json['Address'] = address['address']

    store_name = get_store_name(lines)
    json['Store Name'] = store_name['store_name']

    total_amount = get_total_amount(lines)
    json['Total Amount'] = total_amount['total_amount']

    items =  get_items(lines)
    json['Items'] = items['items']
    print(json)

if __name__=='__main__':
    t1 = time.time()
    imgpath = sys.argv[1]
    run(imgpath)
    t2 = time.time()
    print('time',t2-t1)