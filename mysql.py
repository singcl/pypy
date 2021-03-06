#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "singcl", "123456", "test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("CREATE TABLE IF NOT EXISTS sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

# 使用 fetchone() 方法获取单条数据.
# 使用 fetchall() 方法获取所有数据.
data = cursor.fetchall()

for x in data:
    print(x)

# 关闭数据库连接
db.close()
