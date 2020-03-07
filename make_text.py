import os
from model.ocr import ocr

os.system('mkdir text')
os.system('mkdir parsed_text')

#making folder...
for file in os.listdir('Data'):
    fname = file.split('.')[0]
    os.system('mkdir parsed_text/' + fname)
    text, _ = ocr('Data/' + file)

    with open('text/' + fname, 'w') as f:
        f.writelines(text)


# done only for 415 images...

