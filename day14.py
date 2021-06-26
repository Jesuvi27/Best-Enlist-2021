#1 List down all the error types

1.)NameError
2.)ModuleNotFoundError
3.)IndexError
4.)ZeroDivisionError
5.)ValueError

try:
  raise NameError('python')
except NameError:
  print("The exception demolished")

#ModuleNotFoundError
try: import pandas
 print("Module found")
except:
print("module not found")
#Indexerror
list=list(range(0,6))
try:
  print(list[8])
except:
  print("Error handled")
#ZeroDivisionError
try:
 b=3/0
print(a)
except:
 print("Cannot divide by zero")
#ValueError
try:
  x=int(input("Enter the number"))
except:
  print("It is not a number")
#2 Design a simple calculator app with try and except for all use cas-es

first=int(input("first number:"))
second=int(input("second number:"))
c=input("Enter Operation")
try:
  if (c=='+'):
    print(first+second) 
  elif (c=='-'):
    print(first-second)
  elif (c=='*'):
    print(first*second)
  elif (c=='/'):
    print(first/second)
  else:
    print("enter a valid integer")
except NameError:
 print("Invalid input")
except SyntaxError:
 print("Invalid input")
except TypeError:
 print("Invalid input")
except AttributeError:
 print("Invalid input")
except ValueError:
 print("Invalid input")

OUTPUT:
  first number:4
second number:3
Enter Operation+
7
  
#3print one message if the try block raises a NameError and another for other errors

try:
 raise NameError("python")
except NameError:
 print("The Exception is handled")

OUTPUT:
  The Exception is handled

#4 When try-except scenario is not required

Whenever there is no need for error to be handled or we can let the program to display the error,try-except scenario is not required.

#5Try getting an input inside the try catch block
while True:
 try:
  num=int(input("Enter the integer"))
  print("The integer you have entered is",num)
  break
 except:
  print("Invalid integer")
 print("You have entered an integer")
OUTPUT:
  Enter the integer y
Invalid integer
You have entered an integer
Enter the integer 7
The integer you have entered is 7


