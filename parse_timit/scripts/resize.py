__author__ = 'haseeb'
import os
from PIL import Image as im
from PIL import  Image
from matplotlib import pyplot
import numpy as np

images = "images_list.txt"
output1 = "resized1.png"
output2 = "resized2.png"

w = 512
h = 512


def resize():
    scaler = Image.ANTIALIAS
    images_list_file = open(images, 'r')
    for image_file in images_list_file:
        image_file = image_file[:-1]
        image = im.open(image_file)
        image_res = image.resize((w,h), scaler)
        image_res.save(output2)

if __name__ == '__main__':
    resize()