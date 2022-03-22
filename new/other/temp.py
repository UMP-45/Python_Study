2+#readpic.py
import numpy as np
import struct
import matplotlib.pyplot as plt


 # 读取二进制文件
photo = open('img_1.raw','rb')   
raw_data = photo.read(1048576)
raw_data = struct.unpack('={}f'.format(1048576),raw_data)
image = np.asarray(raw_data).reshape(512,512)
photo.close()
plt.imshow(image, cmap=plt.cm.gray)
plt.show()

#写二进制文件
photo = open('IMG_3586.JPG','wb') 
write_buf = struct.pack('={}4f'.format(image.size),*image.flatten())
photo.write(write_buf)
photo.close()
plt.imshow(image, cmap=plt.cm.jet)
plt.show()

