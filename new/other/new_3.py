#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct

f1 = open('img_1.raw', 'rb')
f2 = open('img_2.raw', 'wb')
try:
    while True:
        data = f1.read(2)
        if not data:
            break
        data = struct.unpack('H',data)
        bit = struct.pack('H',65535-data[0])
        f2.write(bit)
finally:
     f1.close()
     f2.close()