# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:26:49 2019

@author: ASUS ROG
"""

from PIL import Image
import os, sys

path = r"C:\tensorflow1\Speciment\Botol Kaleng dan Plastik\Train\\"
dirs = os.listdir( path )


def resize():
    i = 0 
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((720,540), Image.ANTIALIAS)
            imResize.save('Image_'+str(i)+'.jpg', 'JPEG', quality=90)
            i=i+1
            print("done image " + str(i))

resize()
