#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os

def get_html(url):
    # 返回网页的源代码
    resp = requests.get(url)
    html = resp.text
    return html

def save_html(file_name, file_content):
    # 将网页的源代码保存到本地
    if not os.path.exists(r"{}.html".format(file_name)):
        with open("{}.html".format(file_name), "a+", encoding="utf-8") as f:
            f.write(file_content)
    else:
        with open("{}.html".format(file_name), "a+", encoding="utf-8") as f:
            f.write(file_content)  

urls = ["http://wz.wzljl.cn/?mdl=topic&type=0&orderis=default&status=0&orgid=14&szTypeId=3&page={}".format(i)
       for i in range(1,14)] # 网页的地址

for url in urls:
    html = get_html(url)
    save_html("零距离问政-中国·梧州-市长热线",html)
    print(url) 