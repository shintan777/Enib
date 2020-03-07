import operator 
import sys
import re
import nltk
# from nltk.corpus import stopwords
import os
# import pandas as pd 


def get_date(items):
	#format d/m/y & d-m-y is support
    dates=set()
    # print(items)
    for data in items:
        f1 = re.findall(r'\d{1,2}\(/,.,-)\d{1,2}\/\d{4}',data)
        f2 = re.findall(r'\d{4}\/\d{1,2}\/\d{1,2}',data)
        f3 = re.findall(r'\d{2}\/\d{1,2}\/\d{1,2}',data)
        f4 = re.findall(r'\d{1,2}\/\d{1,2}\/\d{2}',data)
        #TODO: Add "." support i.e 12.12.12, sep/otc/yada        
        for i in f1:
            dates.add(i)
        for i in f2:
            dates.add(i)
        for i in f3:
            dates.add(i)
        for i in f4:
            dates.add(i)
    return dates

def get_invoice_no(data):
    print(data)
    invoice_no = set()
    for i in data:
        if 'invoice' in i.lower().strip().split():
            print(i)
        if 'bill' in i.lower().strip().split():
            print(i)
            for words in i.lower().strip().split():
                try:
                    x = int(words) + 0
                    invoice_no.add(x)
                except:
                    continue
    return invoice_no