from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re


# load the example image and convert it to grayscale
image = cv2.imread('pan_card_decode.png')
ifscre = r'[a-zA-Z]{4}0[a-zA-Z0-9]{6}' 
bankaccre = r'[0-9]{9,18}'

text = pytesseract.image_to_string(image)
print(type(text))
print("*******************************************")
print(re.findall(ifscre,text))
print(re.findall(bankaccre,text))
print("*******************************************")

print(text)
 
# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
cv2.waitKey(0)