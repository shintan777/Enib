from model.extract import get_date, get_invoice_no
import os

for fname in os.listdir('text')[:1]:
    with open('text/' + fname, 'r') as f:
        data = f.readlines()
    folder_name = 'parse_text' + os.sep + fname
    # os.system('mkdir ' + folder_name)
    
    # with open(folder_name+'/date.txt', 'w') as f:
        # print(list(get_date(data)))
        # f.writelines(list(get_date(data)))

    with open(folder_name+'/invoice_no.txt', 'w') as f:
        print(list(get_invoice_no(data)))
        # f.writelines(list(get_date(data)))
        # get_invoice_no(data)