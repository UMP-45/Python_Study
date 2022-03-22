import sqlite3

conn = sqlite3.connect('test.db')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

c = conn.cursor()
print("Opened database successfully")

cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3])

print("Operation done successfully")
conn.close()
#import sqlite3

# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# print("Opened database successfully")

# cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
# for row in cursor:
   # print("ID = ", row[0])
   # print("NAME = ", row[1])
   # print("ADDRESS = ", row[2])
   # print("SALARY = ", row[3])

# print("Operation done successfully")
# conn.close()