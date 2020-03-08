from model.extract import get_date, get_time, get_invoice_no, get_address, get_store_name, get_total_amount, get_items
import os

for fname in sorted(os.listdir('text'))[1:2]:
    print("=========Analysis for file {} ==============".format(fname))
    with open('text/' + fname, 'r') as f:
        data = f.readlines()
    # print(data)
    fname = fname.replace(' ','_')

    # folder_name = 'parse_text' + os.sep + fname
    # os.system('mkdir ' + folder_name)

    # with open(folder_name+'/items.txt', 'w') as f:
    get_items(data)
        # f.writelines(list(get_items(data)))
    
    # with open(folder_name+'/date.txt', 'w') as f:
    #     print(get_date(data))
    #     # f.writelines(list(get_date(data)))

    # with open(folder_name+'/invoice_no.txt', 'w') as f:
    #     print(get_invoice_no(data))
    #     # f.writelines(list(get_invoice_no(data)))
    
    # with open(folder_name+'/address.txt','w') as f:
    #     print(get_address(data))
    #     # f.writelines(list(get_invoice_no(data)))
    # with open(folder_name+'/store_name.txt', 'w') as f:
    #     print((get_store_name(data)))
    #     # f.writelines(list(str(get_store_name(data))))
    # with open(folder_name+'/amout.txt', 'w') as f:
    #     print((get_total_amount(data)))
    #     # 
    # with open(folder_name+'/time.txt', 'w') as f:
    #     print((get_time(data)))
    #     # 
# with open(folder_name+'/date.txt', 'w') as f:
#     print(get_date(data))
#     f.writelines(list(get_date(data)))