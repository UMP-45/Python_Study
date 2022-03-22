import sqlite3

# def prin(cursor):
  # for row in cursor:
    # print("ID = ", row[0],"NAME = ", row[1],"ADDRESS = ", row[2],"SALARY = ", row[3])

conn = sqlite3.connect('test.db') # or (':memory:') or with sqlite3.connect('test.db') as db :
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS COMPANY'
       '(ID INT PRIMARY KEY     NOT NULL,'
       'NAME           TEXT    NOT NULL,'
       'AGE            INT     NOT NULL,'
       'ADDRESS        CHAR(50),'
       'SALARY         REAL);')
conn.commit()
conn.close()
# def drop(conn,table):
  # if table is not None and table != '':
    # sql = 'DROP TABLE IF EXISTS ' + table
    # if SHOW_SQL:
        # print('执行sql:[{}]'.format(sql))
    # cu = get_cursor(conn)
    # cu.execute(sql)
    # conn.commit()
    # print('删除数据库表[{}]成功!'.format(table))
    # close_all(conn, cu)
  # else:
    # print('the [{}] is empty or equal None!'.format(sql))

# drop(conn,COMPANY)

