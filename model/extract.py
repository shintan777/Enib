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
            if j in comp:
                idx = data.index(i)
                break
    ret_me = data[max(0,idx-2):idx+1]
    if ret_me == []:
        ret_me = [i.lower().strip().strip('\n') for i in data[1:5]]
    return {
        'address' : ' '.join(ret_me)
    }

def get_store_name(data):
    existing_stores = os.listdir('Training Data Set')
    existing_stores.append('PHOENIX MALL')
    stores = [i.lower().strip('\n') for i in existing_stores]
    ret_me = []
    idx = 0
    for i in data[:5]:
        comp = i.lower().strip().strip('\n').split()
        for word in comp:    
            if word in stores:
                ret_me = word
                break
    if ret_me == []:
        print("here")
        ret_me = [i.lower().strip().strip('\n') for i in data[1:2]]
        ret_me = ' '.join(ret_me)
    return {
        'store_name' : ret_me
    }
