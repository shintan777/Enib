import operator 
import sys
import re
import os
# import pandas as pd 
import json

def get_date(items):
	#format d/m/y & d-m-y is support
    dates=set()
    for data in items:
        f1 = re.findall(r'\d{1,2}\/\d{1,2}\/\d{4}',data)
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
    return {
        'date_set' : dates
        }

def get_invoice_no(data):
    #get from tanvi

    return {}

def get_address(data):
    with open('utils/cities.txt','r') as f:
        cities = f.readlines()
    cities = [i[3:-3].lower().strip().strip('\n') for i in cities][1:]
    idx = -1
    for j in cities:
        for i in data[:10]:
            comp = i.lower().strip().strip('\n').split()
            if j['City'].lower() in comp:
                idx = data.index(i)
                break
    # print(data[max(0,idx-2):idx+1])
    return data[max(0,idx-2):idx+1]

def get_store_name(data):
    store_name = set()
    existing_stores = os.listdir('Training Data Set')
    existing_stores.append('PHOENIX MALL')
    