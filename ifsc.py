from PIL import Image
import pytesseract
import argparse
import cv2
import os


#print(pytesseract.image_to_string(Image.open('chif.png')))

str1 = pytesseract.image_to_string(Image.open('chif.png'))

print(str1[str1.find('IFSC'):])


    
    image = imread(io.BytesIO(base64.b64decode(d)))

    
    #image = imread(readb64(a,a))
    
    cv2_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite("reconstructed.png", cv2_img)
         
    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    #filename = "tempimg.png"
    #cv2.imwrite(filename, gray)    

    str1 = pytesseract.image_to_string('reconstructed.png')
    
    #print(str1[str1.find('IFSC'):str1.find('IFSC')+18])

    print(str1[str1.find('IFSC'):str1.find('IFSC')+18])    
    

    return str1[str1.find('IFSC'):str1.find('IFSC')+18]
