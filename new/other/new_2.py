#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    r, g, b=rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray=0.2989*r + 0.5870*g + 0.1140*b
    return gray

img=mpimg.imread('img_1.jpg')
plt.imshow(img)
plt.show()
img2=rgb2gray(img)
plt.imshow(img2)
plt.show()