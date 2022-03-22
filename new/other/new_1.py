#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct

f1 = open('img_1.jpg', 'rb')
f2 = open('img_2.jpg', 'wb')
try:
    while True:
        data = f1.read(4)
        if not data:
            break
        data=struct.unpack('i',data)
        bit=struct.pack('i',data[0]+[10,10])
        f2.write(bit)
finally:
     f1.close()
     f2.close()