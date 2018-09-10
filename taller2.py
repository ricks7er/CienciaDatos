# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 12:48:32 2018

@author: jrort
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

image=io.imread("bridge.jpg")

#plt.imshow(image)

xlen = image.size
ylen = image[0].size

b = image[:,:,0]

xlen = b[:,0].size
ylen = b[0].size

dif=50

nm=[b[0:50,0:50],b[50:100,0:50],b[100:150,0:50],
    b[0:50,50:100],b[50:100,50:100],b[100:150,50:100],
    b[0:50,100:150],b[50:100,100:150],b[100:150,100:150],
    b[0:50,150:200],b[50:100,150:200],b[100:150,150:200],
    b[0:50,200:250],b[50:100,200:250],b[100:150,200:250],
    b[0:50,250:300],b[50:100,250:300],b[100:150,250:300]]

nm2=nm
np.random.shuffle(nm2)
b2 = np.concatenate((
        np.concatenate((nm2[0:3]),axis=0),
        np.concatenate((nm2[3:6]),axis=0),
        np.concatenate((nm2[6:9]),axis=0),
        np.concatenate((nm2[9:12]),axis=0),
        np.concatenate((nm2[12:15]),axis=0),
        np.concatenate((nm2[15:18]),axis=0)
        ), axis=1)
#b2=np.concatenate((nm2[0],nm2[1],nm2[2],nm2[3],nm2[4],nm2[5],nm2[6],nm2[7],nm2[8],nm2[9],nm2[10],nm2[11],nm2[12],nm2[13],nm2[14],nm2[15],nm2[16],nm2[17]),axis=0)
plt.imshow(b2)