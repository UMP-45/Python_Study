#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json
from redis_conn import redis_conn_pool

redis_conn = redis_conn_pool()

def get_ncovcity_data():
    url = "http://api.tianapi.com/txapi/ncovcity/index?key=d618ef42861ec00957dcacad6b69e8e0"
    res = requests.get(url).json()
    redis_conn.set("ncovcity_data", json.dumps(res))
    return res

def get_ncov_data():
    url = "http://api.tianapi.com/txapi/ncov/index?key=d618ef42861ec00957dcacad6b69e8e0"
    res = requests.get(url).json()
    redis_conn.set("ncov_data", json.dumps(res))
    return res

def get_trend_data():
    headers = {
        "user-agent":"",
        "accept":""
    }
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total"
    res = requests.get(url, headers=headers).json()
    redis_conn.set("trend", json.dumps(res))
    return res

if __name__ == "__main__":
    """test"""
    trend = get_trend_data()
    print(trend["data"]["areaTree"])
    res = get_ncov_data()
    res2 = get_ncovcity_data()
    print(res["newslist"])
    print("\n")
    print(res2["newslist"][0]["provinceName"])