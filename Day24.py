//1.	Write a Python program to convert a string to datetime 

from datetime import datetime
res = datetime.strptime('Jul 11 2021 11:00PM', '%b %d %Y %I:%M%p')
print(res)

OUTPUT:
2021-07-11 23:00:00

//2.	Write a Python program to subtract five days (last working day) from current date

from datetime import date, timedelta
res = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',res)

OUTPUT:
Current Date : 2021-07-11
5 days before Current Date : 2021-07-6

//3.	Write a Python program to convert the date to datetime using a function 

from datetime import date
from datetime import datetime
res = date.today()
print(datetime.combine(res, datetime.min.time()))

OUTPUT:
2021-07-11 00:00:00

//4.	Write a Python program to print next 7 days (week) starting from today

import datetime

res = datetime.datetime.today()
for i in range(0, 5):
      print(res + datetime.timedelta(days=i))
      
 OUTPUT:
 2021-07-11 19:14:48.150048
2021-07-12 19:14:48.150048
2021-07-13 19:14:48.150048
2021-07-14 19:14:48.150048
2021-07-15 19:14:48.150048
