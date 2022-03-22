#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class sqldb():
  db = False
  dbc = False

  def __init__(self, file) :
    if file == '' : file = ':memory:'
    self.db = sqlite3.connect(file) # or (':memory:') or with sqlite3.connect('test.db') as db :
    self.dbc = self.db.cursor()

  def __del__(self) : self.db.close()
 
  def creater(self, name, sub):
    self.dbc.execute('CREATE TABLE IF NOT EXISTS ' + name + ' (' + sub + ');')
    self.db.commit()

  def insert(self,table, sub) :
    self.dbc.execute('INSERT INTO ' + table + ' ' + sub + ';')
    self.db.commit()

  def updata(self, table, change, item) :
    self.dbc.execute('UPDATE ' + table + ' set ' + change + ' where ' + item )
    self.db.commit()

  def delete(self,table, item) :
    db.execute('DELETE from ' + table  + ' where ' + item + ';')           
    self.db.commit()

  def select(self,table,item) : return self.dbc.execute('SELECT ' + item + ' from ' + table)

   
file = r'./test.db'
obj = sqldb(file)
obj.creater('COMPANY', 'ID INT KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL')
for i in obj.select('COMPANY', 'id, name, address, salary') : print(i[0], i[1], i[2], i[3])
obj.insert('COMPANY', "(ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00)")
for i in obj.select('COMPANY', 'id, name, address, salary') : print(i[0], i[1], i[2], i[3])
obj.updata('COMPANY', 'SALARY = 25000.00', 'ID=1')
for i in obj.select('COMPANY', 'id, name, address, salary') : print(i[0], i[1], i[2], i[3])
#obj.delete()
# obj.show()
'''
def prin(cursor):
  for row in cursor:
    print("ID = ", row[0],"NAME = ", row[1],"ADDRESS = ", row[2],"SALARY = ", row[3])

conn = sqlite3.connect('test.db') # or (':memory:') or with sqlite3.connect('test.db') as db :
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS COMPANY'
       '(ID INT        KEY     NOT NULL,'
       'NAME           TEXT    NOT NULL,'
       'AGE            INT     NOT NULL,'
       'ADDRESS        CHAR(50),'
       'SALARY         REAL);')

print('insert')
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )"); # insert
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit()
cursor = c.execute("SELECT id, name, address, salary  from COMPANY") # prin(cursor)
prin(cursor)

print('updata')
c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1") #updata
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
conn.commit()
# print(conn.total_changes)
prin(cursor)

print('delete:')
c.execute("DELETE from COMPANY where ID=2;") #delete
# print(conn.total_changes)
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
prin(cursor)

conn.commit()
conn.close()
'''

