1.	Create a python module with list and import the module in another .py file and change the value in list

File name:list.py
  l1=[23,14,16,18]
  
File name:temp.py
 
import list1 as li
s=[]
s=li.l1
for i in range(len(s)):
  s[i]+=12
print(s)

OUTPUT:
[35, 26, 28, 30]

2.	Install pandas package (try to import the package in a python file
3.	Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
                            
Answer:
import random
n=random.randint(1,100)
print(n) 
      
OUTPUT:
37
7
16
                            
4.	Import sys package and find the python path
Answer:
                            
import sys,os
f=sys.argv[0]
path_name=os.path.dirname(f)
print(path_name)
