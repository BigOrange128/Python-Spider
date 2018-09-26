import pymysql

db = pymysql.connect(host='localhost', user='root', password='cxc123', port=3306, db='spider')
cursor = db.cursor()
create = "CREATE TABLE IF NOT EXISTS taobao (title VARCHAR(255) NOT NULL, image VARCHAR(255) NOT NULL, price VARCHAR(255) NOT NULL," \
         " shop VARCHAR(255) NOT NULL, location VARCHAR(255) NOT NULL, deal VARCHAR(255) NOT NULL, PRIMARY KEY (shop))"

cursor.execute(create)
db.close()

# 创建表
# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='cxc123', port=3306, db='spider')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()