#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

a = np.array(Image.open("img_1.jpg"))   #图片处于当前文件路径下
print(a.shape)
b = [255,255,255]-a

photo=Image.fromarray(b.astype('uint8'))
photo.save("img_2.jpg")