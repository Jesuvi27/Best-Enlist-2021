Write a Python script to merge two Python dictionaries

Ans:
  a={"apple":"orange","red":"orange"}
  b={"grapes":"banana","voilet":"yellow"}
  c=a|b
  print(c)
  
  OUTPUT:
    {'apple': 'orange', 'red': 'orange', 'grapes': 'banana', 'voilet': 'yellow'}
    
 Write a program to sort the value from descending to ascending in list and convert it in to a set
Ans:
  List=[1,2,7,8,3,4,5]
List.sort()
print("List after sorting : ",List)
Listset=set(List)
print("converted to set : ",Listset)
print()
  
OUTPUT:
  List after sorting :  [1, 2, 3, 4, 5, 7, 8]
converted to set :  {1, 2, 3, 4, 5, 7, 8}

  Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
  Ans:
    #With function
dictionary={'Jobi':4,'Mojo':8,'Julie':6,'Jacky0':4}
a=dictionary.keys()
c=list(a)
c.sort()
print("Sorting keys using function ")
print("{",end="")
for b in range(len(c)):
    print(c[b],":",dictionary[c[b]],",",end="")
print("}")

OUTPUT:
  Sorting keys using function
{Jacky0 : 4 ,Jobi : 4 ,Julie : 6 ,Mojo : 8 ,}

#Without function

dictionary={'Jobi':4,'Mojo':8,'Julie':6,'Jacky0':4}
a=dictionary.keys()
y=list(a)
z=[]
for a in range(len(y)): #sorting wihtout using function
    for j in range(a+1,len(y)):
        if(y[a]>y[j]):
            temp=y[a]
            y[a]=y[j]
            y[j]=temp
print("Sorting keys without function ")
print("{",end="")
for a in range(len(y)):
    print(y[a],":",dictionary[y[a]],",",end="")
print("}")
print()

OUTPUT:
  Sorting keys without function
{Jacky0 : 4 ,Jobi : 4 ,Julie : 6 ,Mojo : 8 }

Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.

a=input("Enter string ")
b=input("Enter substring ")
c=input("Enter string to be replaced ")
d=a.split()
for x in range(len(d)):
    if(d[x]==b):
        d[x]=c
        break
str=""
for ele in d:
    str+=ele
    str+=" "
print("After replacing : ",str)

OUTPUT:
  Enter string Hello Jesuvi
Enter substring Hello
Enter string to be replaced Hi
After replacing :  Hi Jesuvi

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.

J=input("Enter string ")
x=J[0]
y=x.upper()
z=J.replace(x,y)
print("After replacing ",z)
print()

OUTPUT:
  Enter string hello
After replacing  Hello

Write a Python program to find the repeated items of a list

Ans:
  list=[2,3,5,4,3,4,1]
list1=[]
list2=[]
for a in list:

    if(a not in list1):
        list1.append(a)
    else:
        list2.append(a)
print("Repeated items are :",list2)
print()
OUTPUT:
  Repeated items are : [3, 4]
  
 Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
Ans:
  a=6
b=8
c=3
sum=a+b+c
d=int(input("Enter number to be divided"))
print("After dividing the sum : ",sum/d)
print()

OUTPUT:
  Enter number to be divided 4
After dividing the sum :  4.25
  
 Write a Python program to find the Mean,median,mode among three given numbers
Ans:
  import statistics
a=35
b=22
c=13
mean=(a+b+c)/3
list=[a,b,c]
print("Mean of numbers = ",mean)
print("Median of numbers = ",statistics.median(list))
print("Mode of numbers = ",statistics.mode(list))
print()

OUTPUT:
  Mean of numbers =  23.333333333333332
Median of numbers =  22
Mode of numbers =  35

Write a Python program to swap cases of a given string
Ans:
  def swap_case_string(string1):
   result_str = ""   
   for item in string1:
       if item.isupper():
           result_str += item.lower()
       else:
           result_str += item.upper()           
   return result_str
print(swap_case_string("Grapes"))
print(swap_case_string("Guava"))
print(swap_case_string("Mango"))

OUTPUT:
  gRAPES
gUAVA
mANGO
  
Write a program to convert an integer to binary & octa decima
Ans:
x=24
print("Integer : ",x)
print("Binary : ",bin(x))
print("Octa Decimal : ",oct(x))

OUTPUT:
  Integer :  24
  Binary :  0b11000
  Octa Decimal :  0o30

  

  

  
