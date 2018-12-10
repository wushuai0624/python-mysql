#coding=utf-8
from . import mysqlobj
helper= mysqlobj.MysqlHelper(db='test2')

sql='select count(*) from stu where isdelete=0'

row=helper.fetchone(sql)
print (row[0])

