#1	Create a connection for DB and print the version using a python program
import os
import mysql
import mysql.connector

mydb=mysql.connector.connect(host='Local Host',
                             database='database',
                             user='root',
                             password="jes279"
                            )
print(mydb)

#2 Create a employee table and read all the employee name in the table using for loop

import mysql.connector
mydb = mysql.connector.connect(
                               host="localhost",
                               database = "Jesuvi Jeradin",
                               user ="root",
                               password="Jes279"
)

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Employee1 ( EMP_name VARCHAR(255), EMP_no int , EMP_city VARCHAR(255), EMPdep VARCHAR(255))")
dbse.execute("INSERT INTO Employee ( EMP_name, EMP_no, EMP_city, EMPdep) VALUES  ('Harsha',27,'HYD','BI')")
mydb.commit()

dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)

dbse.execute("SELECT * FROM Employee")

for value in dbse:
    print(value)


#3 Create a multiple tables & insert data in table

import mysql.connector
mydb= mysql.connector.connect(host='Local host',
                              database='database',
                              user='root',
                              password='Jes279')

dbse=mydb.cursor()
dbse.excute("CREATE TABLE Employee (Emp_name Jesuvi(25),Emp_no int,Emp_city Jesuvi(259),Emp_dept Jesuvi(25))")
dbse.excute("SHOW Tables")
for value in dbse:
    print(dbse)

    import mysql.connector
mydb= mysql.connector.connect(host='Local host',
                              database='database',
                              user='root',
                              password='Jes279')

dbse=mydb.cursor()
dbse.excute("CREATE TABLE Employee (Emp_name Jesuvi(25),Emp_no int,Emp_city Jesuvi(25),Emp_dept Jesuvi(25))")
dbse.excute("SHOW Tables")
for value in dbse:
    print(dbse)    
