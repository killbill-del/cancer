import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cretaing the Pixel array 

from PIL import Image
from PIL import ImageColor

import os

img_path = '/Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/png_files/'

image_list = []
for entry in os.listdir(img_path):
    if entry.endswith('.png'):
        entry = int(entry.rstrip('.csv.png'))
        image_list.append(entry)
        image_list.sort()

list_img = []
for j in range(len(image_list)):
    stuff = str(image_list[j])+'.csv.png'
    list_img.append(stuff)
#print(list_img[0])

images = [Image.open(img_path+x) for x in list_img]
widths, heights = zip(*(i.size for i in images))
total_height = sum(heights)
max_width = max(widths)
new_im = Image.new('RGB', (max_width, total_height))
y_offset = 0
for im in images:
    new_im.paste(im, (0, y_offset))
    #new_im.transpose(Image.FLIP_LEFT_RIGHT)
    y_offset += im.size[1]
    new_im.save(img_path+'final_result_image.jpg')