1)Write a program to create a list of n integer values and do the following 
• Add an item in to the list (using function)

Ans:

 a= list(range(1,6))
 a.insert(6,7) 
 print(a)

OUTPUT:
  [1, 2, 3, 4, 5, 7]
 

• Delete (using function)

Ans:

 a= list(range(1,6))
 print(a.pop(0))
 print(a)
OUTPUT:
  1
  [2, 3, 4, 5]


• Store the largest number from the list to a variable
Ans:

 x=[7,8,9,5]
 x.sort() 
 y=x[-1] 
 print("the largest number is:",y)
  OUTPUT:
    the largest number is: 9

• Store the Smallest number from the list to a variable
Ans:

 x=[7,8,9,5]
 x.sort()
 y=x[1] 
 print("the smallest number is:",y)
  OUTPUT:
    the smallest number is: 7

Create a tuple and print the reverse of the created tuple 
Ans: 
  my_tuple = [(1,2),(3,4),(5,6)] 
  print(my_tuple[::-1])
    OUTPUT:
      [(5, 6), (3, 4), (1, 2)]

Create a tuple and convert tuple into list 
Ans:
  x=[(1,2),(3,4),(5,6)]
  y=list(sum(x,()))
  print(y)
  OUTPUT:
    [1, 2, 3, 4, 5, 6]
