# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:49:49 2018

@author: Estudiantes
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

d = np.zeros((xlen,ylen))
r = 1
#plt.imshow(b)
#plt.imshow(d)
        
f = np.empty((xlen+2, ylen+2))
f[1:xlen+1, 1:ylen+1] = b

f[0, 1:ylen+1]=b[0, 0:ylen]
f[xlen+1, 1:ylen+1]=b[xlen-1, 0:ylen]
f[1:xlen+1, 0]=b[0:xlen, 0]
f[1:xlen+1, ylen+1]=b[0:xlen, ylen-1]
f[0,0]=b[0,0]
f[0,ylen+1]=b[0,ylen-1]
f[xlen+1, 0]=b[xlen-1,0]
f[xlen+1, ylen+1]=b[xlen-1,ylen-1]

#print('Esta es la imagen original')
plt.imshow(b)

print('que filtro desea cargar?')
numIngr=int(input('1. suavizar 2. suavizado gaussiano 3. bordes horizontales 4. Perfilado'))
if(numIngr==1):
    print('holi')
    for x in range(0,xlen):
        for y in range(0,ylen):
            u=x+1
            w=y+1
            c = [[f[u-r, w-r] , f[u-r, w] , f[u-r, ((w+r) ) ]]]
            c.append([f[u, w-r] , f[u, w] , f[u, ((w+r) )]])
            c.append([f[((u+r) ), w-r] , f[((u+r) ), w] , f[((u+r)),((w+r) )]])
            d[x,y] = np.average(c)
    plt.imshow(d)
elif numIngr==2:       
    d1 = np.zeros((xlen,ylen))
    for x in range(0,xlen):
        for y in range(0,ylen):
            u=x+1
            w=y+1
            c = [[f[u-r, w-r] , 2*(f[u-r, w]) , f[u-r, ((w+r) ) ]]]
            c.append([2*(f[u, w-r]) , 4*(f[u, w]) , 2*(f[u, ((w+r) )])])
            c.append([f[((u+r) ), w-r] , 2*(f[((u+r) ), w]) , f[((u+r)),((w+r) )]])
            d1[x,y] = np.average(c)
    plt.imshow(d1)
elif numIngr==3:
    d2 = np.zeros((xlen,ylen))
    for x in range(0,xlen):
        for y in range(0,ylen):
            u=x+1
            w=y+1
            c = [[-1*(f[u-r, w-r]) , -1*(f[u-r, w]) , -1*(f[u-r, ((w+r) ) ])]]
            c.append([0*(f[u, w-r]) , 0*(f[u, w]) , 0*(f[u, ((w+r) )])])
            c.append([f[((u+r) ), w-r] , f[((u+r) ), w] , f[((u+r)),((w+r) )]])
            d2[x,y] = np.average(c)
    plt.imshow(d2)
elif numIngr==4:        
    d3 = np.zeros((xlen,ylen))
    for x in range(0,xlen):
        for y in range(0,ylen):
            u=x+1
            w=y+1
            c = [[-1*(f[u-r, w-r]) , -1*(f[u-r, w]) , -1*(f[u-r, ((w+r) ) ])]]
            c.append([-1*(f[u, w-r]) , 9*(f[u, w]) , -1*(f[u, ((w+r) )])])
            c.append([-1*(f[((u+r) ), w-r]) , -1*(f[((u+r) ), w]) , -1*(f[((u+r)),((w+r) )])])
            d3[x,y] = np.average(c)
    plt.imshow(d3)

