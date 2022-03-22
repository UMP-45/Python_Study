#-*- coding:utf-8 - *-

import sqlite3
#打开本地数据库用于储存用户信息
conn = sqlite3.connect('./mysql_person.db')

#在该数据库下创建表，创建表的这段代码在第一次执行后需要注释
conn.execute('''CREATE TABLE MT
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME TEXT  TEXT    NOT NULL,
               AGE  INT   NOT NULL,
               ADDRESS CHAR(50),
               SALARY  REAL,
               PhoneNumber INT NOT NULL);''')
print('Table created successfully')

#增加用户信息
def insert():
    USER_NAME = input('请输入用户昵称:')
    cursor = conn.execute("SELECT name from MT where name = '%s';"%USER_NAME)
    for row in cursor:
        if USER_NAME == row[0]:
            print("sorry,该用户名已存在，请重新输入用户名")
            break
    else:
        AGE = int(input('请输入年龄:'))
        ADDRESS = input('请输入用户地址:')
        SALARY = int(input('请输入用户薪水:'))
        PhoneNumber = int(input('请输入联系方式:'))
        sql1 = 'INSERT INTO MT(NAME,AGE,ADDRESS,SALARY,PhoneNumber)'
        sql1 += 'VALUES("%s","%d","%s","%d","%d");'%(USER_NAME,AGE,ADDRESS,SALARY,PhoneNumber)
        conn.execute(sql1)
        conn.commit()
        print("Records insert successfully")

#删除用户信息
def delete():
    delete_name = input("请输入所要删除的联系人姓名:")
    cursor = conn.execute("SELECT name from MT where name = '%s';"%delete_name)
    for row in cursor:
        if delete_name == row[0]:
            conn.execute("DELETE from MT where name = '%s';"%delete_name)
            conn.commit()
            print("Records delete successfully")
    else:
        print("sorry,不存在该用户")

#修改用户信息
def modify():
    update_name = input("请输入要修改用户的姓名:")
    sql6 = "SELECT name from MT where name = '%s';"%update_name
    cursor = conn.execute(sql6)
    for raw in cursor:
        if update_name == row[0]:
            New_addr = input("请输入要修改用户的新地址:")
            New_age = int(input("请输入要修改用户的新年龄:"))
            New_salary = int(input("输入要修改用户的新薪水:"))
            New_num = int(input("请输入要修改用户的新号码:"))
            sql3 = "UPDATE MT set address = '%s',age = '%d',salary = '%d',PhoneNumber = '%d' where name = '%s';"%update_name 
            conn.execute(sql3)
            conn.commit()
            print("修改成功")
            sql5 = "SELECT id, name, age, address, salary, PhoneNumber form MT where name = '%s';"%update_name
            cursor = conn.execute(sql5)
            for row in cursor:
                print("ID = ", row[0])
                print("NAME = ",row[1])
                print("AGE = ",row[2])
                print("ADDRESS = ",row[3])
                print("SALARY = ",row[4])
                print("PhoneNumber = ",row[5],"/n")
                break
    else: print("sorry,不存在该用户")

#查询用户信息
def search():
    conn = sqlite3.connect('mysql_person.db')
    search_name = input('请输入要查询的用户姓名')
    sql2 = "SELECT id, name, age, address, salary, PhoneNumber from MT where name = '%s';"%(search_name)
    cursor = conn.execute(sql2)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ",row[1])
        print("AGE = ",row[2])
        print("ADDRESS = ",row[3])
        print("SALARY = ",row[4])
        print("PhoneNumber = ",row[5],"/n")
        break
    else: print("sorry,没有该用户信息")

#显示所有用户信息
def show_all():
    cursor = conn.execute("SELECT id, name, age, address, salary, PhoneNumber from MT")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ",row[1])
        print("AGE = ",row[2])
        print("ADDRESS = ",row[3])
        print("SALARY = ",row[4])
        print("PhoneNumber = ",row[5],"/n")
    print("Operation done successfully")
    cursor = conn.execute("SELECT count(*) from MT;")
    for row in cursor:
        print("一共有%d个用户"%row[0])

def menu():
    print("1.新增联系人")
    print("2.删除联系人")
    print("3.修改联系人")
    print("4.查询联系人")
    print("5.显示所有联系人")
    print("6.退出程序")
    print("What do you want to do?") 

while True:
    menu()
    x = input("请输入您的选择菜单号:")
    if x == '1':
        insert()
        continue
    if x == '2':
        delete()
        continue
    if x == '3':
        modify()
        continue  
    if x == '4':
        search()
        continue
    if x == '5':
        show_all()
        continue  
    if x == '6':
        print("谢谢使用！")
        exit()
        continue  
    else:
        print("输入的选项不存在，请重新输入")
        continue         

conn.commit()
conn.close()