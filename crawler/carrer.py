#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, time

for page in range(1,10):
    url = "https://careers.tencent.com/tencentcareer/api/post/Query?"
    params = {
        "timestamp":str(time.time()),
        "keyword":"python",
        "pageIndex":page,
        "pageSize":"10",
        "language":"zh-cn",
        "area":"cn"
    } 

    response = requests.get(url, params = params).json()
    print(response["Data"]["Posts"][0]["PostId"])