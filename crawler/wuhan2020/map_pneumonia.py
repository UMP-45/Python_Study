import time, json, requests
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def catch_distribution():
    """抓取行政区域确诊分布数据"""

    data = dict()
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=%d" %int(time.time()*1000)
    for item in json.loads(requests.get(url=url).json()["data"]):
        if item["area"] not in data:
            data.update({item["area"]:0})
        data[item["area"]] += int(item["confirm"])
    
    return data

def catch_daily():
    """抓取每日确诊和死亡数据"""
    
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d"%int(time.time()*1000)
    data = json.loads(requests.get(url=url).json()["data"])
    data.sort(key=lambda x:x['date']) # dict的value排序

    date_list = list() # 日期
    confirm_list = list() # 确诊
    suspect_list = list() # 疑似
    dead_list = list() # 死亡
    heal_list = list() # 治愈
    
    for item in data:
        month, day = item["date"].split("/")
        date_list.append(datetime.strptime("2020-%s-%s"%(month, day), "%Y-%m-%d"))
        confirm_list.append(int(item["confirm"]))
        suspect_list.append(int(item["suspect"]))
        dead_list.append(int(item["dead"]))
        heal_list.append(int(item["heal"]))

    return date_list, confirm_list, suspect_list, dead_list, heal_list

def plot_daily():
    """绘制每日确诊和死亡数据"""

    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily() # 获取数据
    
    plt.figure("2019-nCoV疫情统计图表", facecolor="#f4f4f4", figsize=(10, 8))
    plt.title("2019-nCoV疫情曲线",fontsize=20)

    plt.plot(date_list, confirm_list, label="确诊")
    plt.plot(date_list, suspect_list, label="疑似")
    plt.plot(date_list, dead_list, label="死亡")
    plt.plot(date_list, heal_list, label="治愈")
  
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
    plt.gcf().autofmt_xdate() # 优化标注(自动倾斜)
    plt.grid(linestyle=':') # 显示网格
    plt.rcParams['font.sans-serif']=['SimHei'] # 显示中文
    plt.rcParams['axes.unicode_minus']=False
    plt.legend(loc='best') # 显示图例
    plt.savefig("2019-nCoV疫情曲线_4.3.png") # 保存图片
    plt.show()

# def plot_distribution():
    # """绘制行政区域确诊分布数据"""

    # data = catch_distribution()

if __name__ == "__main__":
    plot_daily()