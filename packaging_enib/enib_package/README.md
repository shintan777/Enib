# EXTRACT NECESSARY INFORMATION BILL (ENIB )
This repository contains solution to the following problem statement by AIDL Hackathon 2020:
- Step 1 : Segmentation of each required field in the bill using semantic segmentation technique.
- Step 2 : Recognition of text in the bills to generate output in the format mentioned below.

To execute the above solution perform the following steps:
run `main.py` as follows
```
$ python main.py <path_to_image>
or
$ python main.py Max_1.jpg
```

Expected output:
```
{'date': '31/12/19', 'time': '7:52', 'invoice_no': '2541014000053141', 'address': 'PHOENIX MARKET CITY,NO. 142 VELACHERY, VELACHERY MAIN ROAD CHENNAI :- 600042', 'store_name': 'big bazaar (future retail ltd)', 'total_amount': '4744'}
```