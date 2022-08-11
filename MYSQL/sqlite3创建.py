import sqlite3
# 导入模块
con = sqlite3.connect('D:/Python/mysql/data.db')
# 创建表
cur = con.cursor()
# 创建游标对象
# print(con)
sql = '''create table t_person(
            pno INTEGER primary key autoincrement,
            pname VARCHAR not null,
            age INTEGER
)'''

try:
    cur.execute(sql)
    print('succeed')
except Exception as e:
    print(e)
    print('fail')
finally:
    cur.close()
    con.close()

