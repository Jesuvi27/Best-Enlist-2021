import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="jes29",
)

mycursor = mydb.cursor()
print(mydb)

dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Employee_Mangement")


dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for x in dbse:
    print(x)

    mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="jes29",
  database="employee_mangement"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for y in dbse:
  print(y)

  dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for y in dbse:
  print(y)

  dbse = mydb.cursor()

sql = "INSERT INTO employee (emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
  ('1','KALAI','16000.0'),
    ('2','ANU','18000.0'),
    ('3','BANU','66700.0'),
    ('4','MANI','45000.0'),
    ('5','ANJU','78000.0'),
    ('6','CHARU','55000.0'),
    ('7','PRIYA','66000.0'),
    ('8','POOVI','54000.0'),
    ('9','BALA','76900.0'),
    ('10','MANO','19000.0'),
    ('11','LENO','54500.0'),
    ('12','BHARATHI','49800.0'),
    ('13','MANOJ','30000.0'),
    ('14','KIRAN','25000.0'),
    ('15','MADDY','17500.0')
       
]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")

mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select max(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for a in myresult:
    print(a)

    mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for a in myresult:
    print(a)

    mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employee")

myresult = mycursor.fetchall()

for a in myresult:
    print(a)

    mycursor = mydb.cursor()

mycursor.execute("SELECT * from employee WHERE EMP_NAME LIKE('JES%')")

myresult = mycursor.fetchall()

for a in myresult:
    print(a)


