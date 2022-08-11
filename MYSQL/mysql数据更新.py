import pymysql
con =pymysql.connect(host='127.0.0.1',user='mgs',password='mgs',database='pymsql_db',port=3306)
cur = con.cursor()
sql = 'update student set sname=%s where sno=%s'  #删除 'delete from student where sname=%s'
try:
    cur.execute(sql,('zhang',1))
    con.commit()
    print('succeful')
except Exception as e:
    print(e)
    con.rollback()
finally:
    con.close()
