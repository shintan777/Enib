import sys
from model.ocr import ocr
from model.extract  import *

def run(imgpath):
    text, lines = ocr(imgpath)
    json = {}

    date = get_date(lines)
    json['date'] = date['date']

    time = get_time(lines)
    json['time'] = time
    
    invoice_no = get_invoice_no(lines)
    json['invoice_no'] = invoice_no

    address = get_address(lines)
    json['address'] = address

    store_name = get_store_name(lines)
    json['store_name'] = store_name

    total_amount = get_total_amount(lines)
    json['total_amount'] = total_amount

    print(json)









if __name__=='__main__':
    imgpath = sys.argv[1]
    run(imgpath)