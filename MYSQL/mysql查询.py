import pymysql
con = pymysql.connect(host='localhost',user='mgs',password='mgs',database='pymsql_db',port=3306)
cur = con.cursor()
sql ='select * from student'  #拆入insert
try:
    cur.execute(sql)
    students = cur.fetchall()
    print(students)
except Exception as e:
    print(e)
    print('failure')
finally:
    cur.close()
    con.close()