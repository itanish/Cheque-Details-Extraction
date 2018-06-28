from PIL import Image
import pytesseract
import argparse
import cv2
import os
from flask import Flask
from flask import request
from skimage.segmentation import clear_border
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import base64
import json
from PIL import Image
from flask import Flask
from flask import request
import re
 
app = Flask(__name__)


@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    
    ifscre = r'[a-zA-Z]{4}0[a-zA-Z0-9]{6}' 
    bankaccre = r'[0-9]{9,18}'
    
    print (request.is_json)
    content = request.get_json()
    a = content['image']
    

    str1 = pytesseract.image_to_string(readb64(a,a))
    
    #print(str1[str1.find('IFSC'):str1.find('IFSC')+18])

    #print(str1[str1.find('IFSC'):str1.find('IFSC')+18])  
    
    
    data = {
        'IFSC': re.findall(ifscre,str1),
        'Account Number': re.findall(bankaccre,str1)
    }

    json_data = json.dumps(data)
    print(str1)    
    
    
    
    return json_data
    

    return str1[str1.find('IFSC'):str1.find('IFSC')+18]



def readb64(base64_string,a):
    fh = open("imageToSave1.png", "wb")
    fh.write(base64.b64decode(a))
    fh.close()
    pimg = Image.open('imageToSave.png')
    return pimg


if __name__ =='__main__':
    app.run(host='0.0.0.0', port= 8091)
