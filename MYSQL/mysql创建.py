import pymysql
# 创建
con = pymysql.connect(host='localhost',user='mgs',password='1mgs',database='pymsql_db',port=3306)
# print(con)
cur = con.cursor()
sql = '''
    create table student(
    sno int primary key auto_increment,
    sname varchar(30) not null,
    age int(2),
    score float(3,1)
    )
'''
try:
    cur.execute(sql)
except Exception as e:
    pass
finally:
    pass