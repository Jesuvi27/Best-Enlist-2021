//1.	Create a JSON of all object types and import the JSON into a SQL Database

import json

x=[
     {'First_name':"Jenni",Last_name':"Mol",'age':21,'Student':True,'Percentage':87.9,'Group':'Biology'},
     {'First_name':"kalai",Last_name':"Mani",'age':20,'Student':True,'Percentage':98.9,'Group':"ComputerScience"},
     {'First_name':"Rohan",Last_name':"raj",'age':20,'Student':True,'Percentage':87.8,'Group':'Biology'},
     {'First_name':"Vijay",Last_name':"Kumar",'age':20,'Student':True,'Percentage':93.0,'Group':'Biology'},
     {'First_name':"Shakthi",Last_name':"Vel",'age':20,'Student':True,'Percentage':67.0,'Group':'ComputerScience'}
     {'First_name':"Vasanth",Last_name':"Kumar",'age':20,'Student':True,'Percentage':77.8,'Group':'Biology'}
]


rs =json.dumps(x)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jes22"
)

print(mydb)
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE JSONFIL")
dbse = mydb.cursor()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jes22",
  database="jsonfil"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE stud (First_name VARCHAR(255),Last_name VARCHAR(255),age INT, Student VARCHAR(255), Percentage DOUBLE, Group VARCHAR(255))")

dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for a in dbse:
  print(a)

dbse = mydb.cursor()
dbse.execute("SHOW COLUMNS FROM stud")

for a in dbse:
  print(a)

