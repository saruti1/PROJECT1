import cx_Oracle
con=cx_Oracle.connect("system/Cdac1234@localhost:1521/orcl.17.0.195")
cursor = con.cursor()
cursor.execute("insert into employee(Empid,Ename,salary,deptid) values(6,'Sachin',98000,20)")
con.commit()
print("Record inserted successfully")
cursor.close()
con.close()
