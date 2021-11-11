#Author: Priyanshu Jain
# Date: 09.11.21
"""This is a script which rotates all the images 90 degrees clockwise and change the resolution
 of each image to 128*128 pixels."""

import PIL
import os
from PIL import Image


mypath = "C:/Users/Lenovo/Desktop/Images/"
newpath = "C:/Users/Lenovo/Desktop/Converted/"

#def convertImage(file):
    #im = Image.open(file)
    #print("The size of {} is {}".format(file, im.size))
    #f, e = os.path.splitext(file)
    #print("File: {} Ext: {}".format(f,e))
    

def rotateImage(file):
    print(file)
    f, e = os.path.splitext(file)
    im = Image.open(mypath+file).convert('RGB')
    ex = ".jpg"
    savename = newpath+f+ex
    im.rotate(-90).resize((128,128)).save(savename)
    

for filename in os.listdir(mypath):
    file = os.path.join(mypath, filename)
    if os.path.isfile(file):
        #print(filename)
        rotateImage(filename)