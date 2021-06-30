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

#3 Create a employee table and read all the employee name in the table using for loop

import mysql.connector
mydb = mysql.connector.connect(
                               host="localhost",
                               database = "Jenni",
                               user ="root",
                               password="Jes279"
)

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Employee1 ( EMP_name VARCHAR(255), EMP_no int , EMP_city VARCHAR(255), EMPdep VARCHAR(255))")
dbse.execute("INSERT INTO Employee ( EMP_name, EMP_no, EMP_city, EMPdep) VALUES  ('jenni',27,'KK','BI')")
mydb.commit()

dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)

dbse.execute("SELECT * FROM Employee")

for value in dbse:
    print(value)


#2 Create a multiple tables & insert data in table

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="jes27",
  database="database11"
)
dbse = mydb.cursor()
dbse.execute("CREATE employee table(Employee_name VARCHAR(255), Employee_id int,Employee_dep VARCHAR(255))")
dbse = mydb.cursor()
dbse.execute("CREATE TABLE staff (name VARCHAR(255), id int ,city VARCHAR(255))")
dbse =mydb.cursor()
dbse.execute("CREATE TABLE seniors(reg INT(24) , name VARCHAR(255) , dob INT(19))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for i in dbse:
  print(i)    
