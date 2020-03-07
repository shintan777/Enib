import os
import cv2
root ='Data'
lis = os.listdir(root)

os.system('mkdir json')

for files in lis:
    file_name,ext = files.split('.')
    new_file = file_name + '.json'
    img = cv2.imread('Data/' + files)
    height, width, _ = img.shape
    my_str = { "name" : "enib", "bnbbox" : {'xmin':0, 'ymin':0, 'xmax':width, 'ymax':height} }
    write_this = '[' + str(my_str) + ']'
    # print(write_this)
    with open('json/' + new_file, 'w') as f:
        f.write(write_this)
    f.close()
