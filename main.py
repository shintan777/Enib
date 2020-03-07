import sys
from model.ocr import ocr
from model.extact  import *

def run(imgpath):
    text, lines = ocr(imgpath)
    



if __name__=='__main__':
    imgpath = sys.argv[1]
    run(imgpath)