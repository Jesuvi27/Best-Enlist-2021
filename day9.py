•	Write a program to loop through a list of numbers and add +2 to every value to elements in list
ANS:
  list=[2,4,6,8,2]
list1=[]
for a in list:
    b=a+2
    list1.append(b)
print("After adding 2 to list is ",list1)
print()

OUTPUT:
  After adding 2 to list is  [4, 6, 8, 10, 4]
  
  .Write a program to get the below pattern 54321 4321 321 21 1

Ans:

r=int(input("Enter the no of rows:"))
for i in range(0,r+1): 
  for j in range(r-i,0,-1):
    print(j,end="") 
    print()

3.Python Program to Print the Fibonacci sequence
  
  Python Program to Print the Fibonacci sequence

 ANS:
 x=int(input("Enter number of terms "))
print("Fibonacci Series")
a=0
b=1
print(a,end=" ")
for i in range(x-1):
    c=a+b
    print(a,end=" ")
    a=b
    b=c
print()

OUTPUT:
  Enter number of terms 10
Fibonacci Series
0 0 1 1 2 3 5 8 13 21

Explain Armstrong number and write a code with a function
ANS:
  print()
x=407
y=x
a=0
while(x>0):
   z=x%10
   m=z*z*z
   a+=m
   x//=10

if(a==y):
    print(y," is a armstrong number")
OUTPUT:
  407  is a armstrong number
  
5.Write a program to print the multiplication table of 9

Ans: n=9 
     for i in range(1,11): 
      print(n,"x",i,"=",n*i)
      
    OUTPUT:
      9 x 1 = 9
      9 x 2 = 18
      9 x 3 = 27
      9 x 4 = 36
      9 x 5 = 45
      9 x 6 = 54
      9 x 7 = 63
      9 x 8 = 72
      9 x 9 = 81
      9 x 10 = 90
 

6.Check if a program is negative or positive

Ans:

n=int(input ("Enter the number:"))
if n>0: 
  print("the no is positive") 
else: 
  print("the no is negative")
  
 OUTPUT:
  Enter the number:1
the no is positive

Enter the number:-1
the no is negative

7.Write a program to convert the number of days to ages Ans:

Days=int(input("enter the number of days:")) 
years=int(Days/365) 
print("Days to years=",years)

OUTPUT:
  enter the number of days:455
  Days to years= 1

8.Solve Trigonometry problem using math function write a program to solve using math function

Ans:

import math a=math.pi/3
b=2 
c=4 
print("the cosine value of pi/3 is:") 
print(math.cos(a)) 
print("the hypotenuse value of 2 and 4 is:") 
print(math.hypot(b,c))

OUTPUT:
  the cosine value of pi/3 is:
0.5000000000000001
the hypotenuse value of 2 and 4 is:
4.47213595499958

9.Create a calculator only on a code level by using if condition (Basic arithmetic calculation)

Solution:

print("Calculator")
print(" 1.Addition")
print(" 2.Subraction") 
print(" 3.Multiplication") 
print(" 4.Division") 
choice=int(input("enter your choice:"))
if choice==1: 
 x=int(input("enter the first no:")) 
 y=int(input("enter the second no:")) 
 z=x+y 
 print("Sum=",z) 
elif choice==2: 
  x=int(input("enter the first no:")) 
  y=int(input("enter the second no:")) 
  z=x-y 
  print("Differnce",z) 
elif choice==3: 
  x=int(input("enter the first no:")) 
  y=int(input("enter the second no:")) 
  z=x*y
  print("Product",z) 
elif choice==4:
  x=int(input("enter the first no:")) 
  y=int(input("enter the second no:")) 
  z=x/y 
  print("Quotient",z) 
else: 
  print("Invalid choice!!")


  OUTPUT:
    Calculator
 1.Addition
 2.Subraction
 3.Multiplication
 4.Division
enter your choice:3
enter the first no:3
enter the second no:4
Product 12
    
