//Write a Python multithreading program to print current date.
#1. Define a subclass using threading.Thread class.

from threading import *
from time import *
from datetime import date,datetime
class thread1(Thread):
    def run(self):
        print(date.today())
        sleep(0.1)
        
class thread2(Thread):
    def run(self):
        print(datetime.today())
        sleep(1)
  

#2. Instantiate the subclass and trigger the thread.

x = thread1()
x.start()
y=thread2()
y.start()
print("\nMain Thread ")

OUTPUT:
2021-07-14
2021-07-14 13:09:12.079311

Main Thread 
