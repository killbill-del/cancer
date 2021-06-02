#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:18:07 2020

@author: Gopal Narayan Srivastava
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cretaing the Pixel array 

from PIL import Image
import numpy as np

import os
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
# Reading the dataset
print("\n\t\t\tPlease wait! We are processing the data\n\n")
path = '/Volumes/MY_PASSPORT/JRF/cancer_genome/cancer'

# red = 108

for entry in os.listdir(path):
    if entry.endswith('.csv'):
        dataset = pd.read_csv(entry)
        X = dataset.iloc[:].values
        C = dataset.iloc[:,0].values
        #print(entry)
        #print(len(C))
        G = labelencoder_X_1.fit_transform(X[:,1])
        #print(len(G))
        xx = 0
        pro = 0
        proz = 0
        ddd = []
        while xx<len(G):
            cvb = G[xx]
            for ff in range(len(G)):
                if(cvb==G[ff]):
                    pro += 1
                    proz += 1
            ddd.append(pro)
            xx = proz
            pro = 0
        #print(ddd)
        delta = []
        c = 0
        c1 = C[0]
        for f in range(1):
            delta.append(0)
        #print(delta)
        for p in range(len(C)):
            if(C[p]== c1):
                c += 1
            #delta[c1-1] = c
            delta[0] = c
        #print(delta) 
        
        import numpy as np
        from PIL import Image

        def color(x,y,s):
            for i in range(x, x+s):
                for j in range(y, y+s):
                    k[i,j] = (192, 192, 192)  #why is k not returned?
            return(k)

        k = np.zeros((110, 1050, 3), dtype=np.uint8)+255
        #k = np.zeros((810, 200, 3), dtype=np.uint8)
        #k.ravel()[delta] = 255
        #print(k)
        #color(0,0,5)
        l=0
        p=0
        ctr = 0
        for ll in range(delta[0]):
            for i in range(len(ddd)):
                if ctr <= int(delta[0]):
                    num_patch = int(ddd[i])
                    for z in range(num_patch):
                        #print(z)
                        color(l,p,5)
                        l += 10
                        if (z+1)%10 == 0:
                            p += 10
                            l = 0
                    #ll += 1
                    l = 0
                    p = p + 10
                ctr += int(ddd[i])
            l += 10
            p = 0
        img = Image.fromarray(k, 'RGB')
        img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT).save(entry+'.png')

#https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
image_list = []
for entry in os.listdir(path):
    if entry.endswith('.png'):
        image_list.append(entry)
    #print(image_list)
images = [Image.open(x) for x in image_list]
widths, heights = zip(*(i.size for i in images))
total_height = sum(heights)
max_width = max(widths)
new_im = Image.new('RGB', (max_width, total_height))
y_offset = 0
for im in images:
    new_im.paste(im, (0, y_offset))
    #new_im.transpose(Image.FLIP_LEFT_RIGHT)
    y_offset += im.size[1]
new_im.save('combined_dataset_image.jpeg')
print("\t\t\tProcessing is done.\n\t\t\tPlease go to the work directory for the image\n")

'''


total_width = sum(widths)
max_height = max(heights)
new_im = Image.new('RGB', (total_width, max_height))
x_offset = 0
for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]
new_im.rotate().transpose(Image.FLIP_LEFT_RIGHT).save('combined_dataset_image.jpg')
print("\t\t\tProcessing is done.\n\t\t\tPlease go to the work directory for the image\n")
'''