import numpy as np
import matplotlib.pyplot as plt

# import Tkinter
# top = Tkinter.Tk()
# # 进入消息循环
# top.mainloop()

plt.figure(1,dpi=50)
x= np.linspace(-np.pi,np.pi,100) # x轴的定义域为 -3.14~3.14，中间间隔100个元素
plt.plot(x,np.sin(x))
plt.show()

