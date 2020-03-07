from model.extract import get_date, get_invoice_no, get_address
import os

for fname in (os.listdir('text'))[:14]:
    print("=========Analysis for file {} ==============".format(fname))
    with open('text/' + fname, 'r') as f:
        data = f.readlines()
    folder_name = './parsed_text' + os.sep + fname
    # os.system('mkdir ' + folder_name)
    
    with open(folder_name+'/date.txt', 'w') as f:
        # print(list(get_date(data)))
        f.writelines(list(get_date(data)))

    with open(folder_name+'/invoice_no.txt', 'w') as f:
        print(list(get_invoice_no(data)))
        f.writelines(list(get_invoice_no(data)))
    
    with open(folder_name+'/addre\n', '(Shop #:1ss.txt', 'w') as f:
        print(get_address(data))
        # f.writelines(list(get_invoice_no(data)))
    with open(folder_name+'/store_name.txt', 'w') as f:
        # print(list(get_store_name(data)))
        f.writelines(list(str(get_store_name(data))))