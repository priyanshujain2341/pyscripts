#!/usr/bin/env python3

import PIL
from PIL import Image
import os



mypath = "supplier-data/images/"
newpath = "supplier-data/images/"


def convertImage(file):
	f, e = os.path.splitext(file)
	im = Image.open(mypath+filename).convert("RGB")
	ex = ".jpeg"
	savename = newpath + f + ex
	im.resize((600,400)).save(savename)


for filename in os.listdir(mypath):
    file = os.path.join(mypath, filename)
    if os.path.isfile(file):
        #print(filename)
        convertImage(filename)