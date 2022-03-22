import csv
from matplotlib import pyplot as plt
from datetime import datetime

def get_file(filename): 
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        total_box, split_total_box, query_date = [],[],[]
        for row in reader:
            try:
                total = float(row[0]) # csv数据需显示转换，否则数据格式不正确
                split_total = float(row[1]) 
                query = datetime.strptime(row[2], "%Y-%m-%d")
            except ValueError:
                pass
            else:
                total_box.append(total)
                split_total_box.append(split_total)
                query_date.append(query)
    return total_box, split_total_box, query_date

def my_plot(x,y_1,y_2):
    fig=plt.figure()
    plt.plot(x,y_1,color="red",label="total box")
    plt.plot(x,y_2,label="spilt total box",color="blue")
    plt.legend(loc='upper right')
    plt.title("box office(2018.1.1-2018.1.31)")

    plt.xlabel("日期")
    plt.ylabel("票房/万")
    plt.rcParams['font.sans-serif']=['SimHei'] # 显示中文
    plt.rcParams['axes.unicode_minus']=False

    fig.autofmt_xdate() # 为了避免X轴日期显示彼此重叠，调用该方法，将以倾斜的形式显示日期标签
    
    plt.savefig("box_office.png") # 保存需在显示前面，否则保存的图片为空白
    plt.show()

if __name__ == "__main__":
    total_box, split_total_box, query_date = [],[],[]
    total_box, split_total_box, query_date = get_file("total_data.csv")
    my_plot(query_date, total_box, split_total_box)