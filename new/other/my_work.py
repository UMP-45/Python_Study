#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import struct

# arr = np.array(Image.open("img_1.jpg"))
# shape = arr.shape  #(1080, 1920, 3)
# size  = arr.size   #6220800
# print(size)
file = open("img_1.jpg","rb")
raw_data = file.read() #type(raw_data) 为bytes
#raw_data = struct.unpack('={}i'.format(1048576),raw_data)
#a = np.array(raw_data)
a = list(raw_data)
#print(a)
for i in range(len(a)):
  a[i] += 50
  i += 1

file.close()

