#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://automatetheboringstuff.com/chapter17/#calibre_link-134
#https://note.nkmk.me/en/python-pillow-concat-images/
"""
Created on Nov 5, 2020

@author: Gopal Narayan Srivastava
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cretaing the Pixel array 

from PIL import Image
from PIL import ImageColor

import os
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()

#from cv2 import cv2

#from google.colab.patches import cv2_imshow
# Reading the dataset
path = '/Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/csv_files/'
#img_path = '/Volumes/MY_PASSPORT/JRF/cancer_genome/gopal_gen_copy/png_files/'
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
    for entry in range(1,24):
        if (list(line)[0] == entry):
            dataset = pd.read_csv(path+str(entry)+'.csv')
            X = dataset.iloc[:].values
            G = dataset['Gene name'].value_counts().sort_index()
            id = G.index
            for i in range(len(G)):
                #if list(line)[1] == id[i]:
                d1 = dataset[dataset['Gene name']==id[i]]
                d1.to_csv(test_found+str(entry)+'.'+id[i]+'.csv', index = False)

for line in X_test:   
    for entry in os.listdir(test_found):
        if entry.endswith('.csv'):
            dataset = pd.read_csv(test_found+entry)
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
        
            def color(x,y,s):
                for i in range(x, x+s):
                    for j in range(y, y+s):
                        k[i,j] = (192, 192, 192)  #why is k not returned?
                return(k)

            k = np.zeros((110, 350, 3), dtype=np.uint8)+255
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
            img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT).save(test_found+entry+'.png')