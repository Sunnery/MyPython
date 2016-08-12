#coding=utf-8
'''
Created on 2016-8-12

@author: 研发
'''
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='jerry',
        )
cur = conn.cursor()
aa=cur.execute("select * from pokemon")
print aa

#打印表中的多少数据
info = cur.fetchmany(aa)
for ii in info:
    print ii
cur.close()
conn.commit()
conn.close()