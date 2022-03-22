#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os

file = open("零距离问政-中国·梧州-书记信箱.html", mode='r', encoding="utf-8")
text = file.read() # 打开文件
res = r'<tr>(.*?)</tr>'
data = re.findall(res, text, re.S|re.M) # 过滤html中的标签 

def save_to_csv(data):
    # 将数据保存为excel文件
    if not os.path.exists(r"零距离问政-中国·梧州-书记信箱.csv"):
        with open("零距离问政-中国·梧州—书记信箱.csv", "a+", encoding="utf-8") as f:
            f.write("编号,性质,标题,受理单位,作者,时间,状态,评论/点击\n")
            for d in data:
                try:
                    d = my_format(d)
                    if d[0] == "编号":  
                        pass
                    else:
                        row = "{},{},{},{},{},{},{},{}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])
                        f.write(row)
                        f.write('\n')
                except:
                    raise
    else:
        with open("零距离问政-中国·梧州-书记信箱.csv", "a+", encoding="utf-8") as f:
            for d in data:              
                try:
                    d = my_format(d)
                    if d[0] == "编号": 
                        pass
                    else:
                        row = "{},{},{},{},{},{},{},{}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])
                        f.write(row)
                        f.write('\n')
                except:
                    raise
    print("save finish!")

def my_format(data):
    # 格式化数据  
    data = re.sub('<[^>]+>', " ", data).strip()
    data = re.split(r'\s+',data)
    #print(data))
    return data

if __name__ == "__main__":
    save_to_csv(data)