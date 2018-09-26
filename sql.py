#插入数据如果重复则更新
import pymysql

data = {
    'id':'20120001',
    'name':'Bob',
    'age':20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update

db = pymysql.connect(host='localhost', user='root', password='cxc123', port=3306, db='spider')
cursor = db.cursor()
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()


#创建数据库
# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='cxc123', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spider DEFAULT CHARACTER SET utf8")
# db.close()

# 创建表
# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='cxc123', port=3306, db='spider')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

#删除数据
# table = 'students'
# condition = 'age > 20'
#
# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()

#查询数据
# sql = 'SELECT * FROM students WHERE age >= 20'
# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount)
#     row = cursor.fetchone()#获取第一个数据，再次调用移动指针
#     while row:
#         print('Row:', row)
#         row = cursor.fetchone()
# except:
#     print('Error')