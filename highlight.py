#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://automatetheboringstuff.com/chapter17/#calibre_link-134
#https://note.nkmk.me/en/python-pillow-concat-images/
"""
Created on Wed Nov 5, 2020

@author: Gopal Narayan Srivastava
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cretaing the Pixel array 

from PIL import Image
from PIL import ImageColor

import os

img_path = '/Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/png_files/'
test_path = '/Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/test_file/'
test_found = '/Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/test_found/'
#test_name = input("Please enter the name of the test csv file: ")

try:
    test = pd.read_csv(test_path+'test.csv')
except:
    print("\nTest file either doesn't exist or file name is wrong\n")
    print("Please input a valid test file name with csv extension\n")

X_test = test.iloc[:].values
#print(X_test)
locations = 0
count = 0
for line in X_test:
    gene = list(line)[1]
    #print(gene)
    mutation = list(line)[3]
    #print(mutation)
    for entry in os.listdir(test_found):
        if entry.endswith('.csv'):
            entry1 = entry.rstrip('.csv')
            #print(entry)
            e = entry1.find('.')
            #print(e)
            if gene == entry1[2:] and e==1:
                #print(entry)
                dataset = pd.read_csv(test_found+entry)
                X = dataset.iloc[:].values
                #print(X)
                for m in range(0, len(X[:,0])):
                    if X[m,3] != mutation:
                        count += 1
                    elif X[m,3] == mutation:
                        locations = count + 1
                print(locations)
                entry1 = entry.rstrip('.csv.png')
                if gene == entry1[2:]:
                    #print(gene)
                    print(entry1[2:])
                    #print(test_found+entry+'.png')
                image = Image.open(test_found+entry+'.png')
                width, height = image.size
                #print(width, height)
                if locations%10 != 0:
                    x = locations - (locations%10)
                    y = int(109-(((locations%10)*10)-10))
                    for i in range(x, x+5):
                        for j in range(y, y-5, -1):
                            image.putpixel((i,j), ImageColor.getcolor('red', 'RGB'))
                            image.save(test_found+entry+'.png')
                elif locations%10 == 0:
                    x = locations - 10
                    y = 19
                    for i in range(x, x+5):
                        for j in range(y, y-5, -1):
                            image.putpixel((i,j), ImageColor.getcolor('red', 'RGB'))
                            image.save(test_found+entry+'.png')
                else:
                    break
                locations = 0
                count = 0
            elif (gene == entry1[3:]) and (e==2):
                #print(entry)
                dataset = pd.read_csv(test_found+entry)
                X = dataset.iloc[:].values
                #print(X)
                for m in range(0, len(X[:,0])):
                    if X[m,3] != mutation:
                        count += 1
                    elif X[m,3] == mutation:
                        locations = count + 1
                print(locations)
                entry1 = entry.rstrip('.csv.png')
                #print(entry1)
                if gene == entry1[3:]:
                    print(gene)
                    #print(entry1[3:])
                    #print(test_found+entry+'.png')
                image = Image.open(test_found+entry+'.png')
                width, height = image.size
                #print(width, height)
                if locations%10 != 0:
                    x = locations - (locations%10)
                    y = int(109-(((locations%10)*10)-10))
                    for i in range(x, x+5):
                        for j in range(y, y-5, -1):
                            image.putpixel((i,j), ImageColor.getcolor('red', 'RGB'))
                            image.save(test_found+entry+'.png')
                elif locations%10 == 0:
                    x = locations - 10
                    y = 19
                    for i in range(x, x+5):
                        for j in range(y, y-5, -1):
                            image.putpixel((i,j), ImageColor.getcolor('red', 'RGB'))
                            image.save(test_found+entry+'.png')
                else:
                    break
            locations = 0
            count = 0
        else:   
            continue

image_list = []
for entry in os.listdir(test_found):
    if entry.endswith('.png'):
        image_list.append(test_found+entry)
        image_list.sort()
        entry1 = entry.rstrip('.csv.png')
        e = entry1.find('.')
        if e == 1:
            #print(e)
            images = [Image.open(x) for x in image_list]
            widths, heights = zip(*(i.size for i in images))
            total_width = sum(widths)
            max_height = max(heights)
            new_im = Image.new('RGB', (total_width, max_height))
            x_offset = 0
            for im in images:
                new_im.paste(im, (x_offset,0))
                #new_im.transpose(Image.FLIP_LEFT_RIGHT)
                x_offset += im.size[0]
            new_im.save(str(img_path+entry[0])+'.csv.png')
            #print(locations)
        elif e == 2:
            images = [Image.open(x) for x in image_list]
            widths, heights = zip(*(i.size for i in images))
            total_width = sum(widths)
            max_height = max(heights)
            new_im = Image.new('RGB', (total_width, max_height))
            x_offset = 0
            for im in images:
                new_im.paste(im, (x_offset,0))
                #new_im.transpose(Image.FLIP_LEFT_RIGHT)
                x_offset += im.size[0]
            new_im.save(str(img_path+entry[0:2])+'.csv.png')
