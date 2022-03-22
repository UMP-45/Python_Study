#-*- coding:utf-8 -*-
import sqlite3
#打开本地数据库用于存储用户信息
conn = sqlite3.connect('mysql_person.db')

#在该数据库下创建表，创建表的这段代码在第一次执行后需要注释掉，否则再次执行程序会一直提示：该表已存在
conn.execute('''CREATE TABLE MT
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";
conn.close()

#增加用户信息
def insert():
    ID = input('请输入用户ID:\n')
    NAME = raw_input('请输入用户昵称:\n')
    AGE = input('请输入年龄:\n')
    ADDRESS = raw_input('请输入用户地址:\n')
    SALARY = input('请输入用户薪水:\n')
    sql1 = 'insert into MT(ID,NAME,AGE,ADDRESS,SALARY)'
    sql1 += 'values("%d","%s","%d","%s","%d");'%(ID,NAME,AGE,ADDRESS,SALARY)
    conn.execute(sql1)
    conn.commit()
    print "Records insert successfully"

#删除用户信息
def delete():
    name = raw_input("请输入所要删除的联系人姓名:")
    cursor = conn.execute("SELECT name from MT where name = '%s';"%name)
    for row in cursor:
        if name == row[0]:
            conn.execute("DELETE from MT where name = '%s';"%name)
            conn.commit()
            print "Records delete successfully"
            break
    else:
        print "sorry,不存在该用户"

#修改用户信息
def modify():
    name = raw_input("请输入要修改用户的姓名:")
    print search()
    sql4 = "SELECT id, name, age,address, salary  from MT where name = '%s';"%name
    cursor = conn.execute(sql4)
    x = raw_input("请输入要修改用户的新地址:")
    y = input("请输入要修改用户的新年龄:")
    z = input("请输入要修改用户的新薪水:")
    sql3 = "UPDATE MT set address = '%s',age = '%d',\
        salary = '%d' where name = '%s';"%(x,y,z,name)
    conn.execute(sql3)
    conn.commit()
    print "修改成功"
    sql5 = "SELECT id, name, age,address, salary  from MT where name = '%s';"%name
    cursor = conn.execute(sql5)
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "AGE = ",row[2]
        print "ADDRESS = ", row[3]
        print "SALARY = ", row[4], "\n"


#查询用户信息
conn = sqlite3.connect('mysql_person.db')

def search():
    conn = sqlite3.connect('mysql_person.db')
    name = raw_input('请输入要查询的用户姓名')
    sql2 = "SELECT id,name,age, address, salary from MT where name= '%s';" % (name)
    cursor = conn.execute(sql2)
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "AGE = ",row[2]
        print "ADDRESS = ", row[3]
        print "SALARY = ", row[4], "\n"
        break
    else:
        print "sorry,没有该用户信息"

#显示所有用户信息
def showall():
    cursor = conn.execute("SELECT id, age, name, address, salary  from MT")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "AGE = ",row[2]
        print "ADDRESS = ", row[3]
        print "SALARY = ", row[4], "\n"
    print "Operation done successfully";
    cursor = conn.execute("select count(*) from MT;")
    for row in cursor:
        print "一共有%d个用户"%row[0]

def menu():
    print '1.新增联系人'
    print '2.删除联系人'
    print '3.修改联系人'
    print '4.查询联系人'
    print '5.显示所有联系人'
    print '6.退出程序'
    print 'What do you want to do?'
while True:
    menu()
    x = raw_input('请输入您的选择菜单号:')
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
        showall()
        continue
    if x == '6':
        print "谢谢使用！"
        exit()
        continue
    else:
        print "输入的选项不存在，请重新输入！"
        continue
