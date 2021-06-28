#1 Create a lambda function that multiplies argument x with argument y

mul = lambda x,y: x*y
print(mul(4,6))


OUTPUT:
24

#2 Write a Python program to create Fibonacci series to n using Lambda

def fib(x):
	y= [0, 2]
	any(map(lambda _: y.append(sum(y[-4:])),range(4, x)))
	return y[:x]   
print(fib(7))


OUTPUT:
    [0, 2, 2, 4, 8]


#3 Write a Python program that multiply each number of given list with a given number 
x=[1,2,3,4,5]
print("Original list:", x)
y=2
print("Given number:", y)
a=map(lambda number:number*y,x)
print(','.join(map(str,a)))


OUTPUT:
Original list: [1, 2, 3, 4, 5]
Given number: 2
2,4,6,8,10


#4 Write a Python program to find numbers divisible by 9 from a list of numbers 
x =[18,81,45,76,33,54]
print("Orginal list:",x)
res = list(filter(lambda y: (y % 9 == 0 ), x)) 
print("\nNumbers of the above list divisible by nine:",res)


OUTPUT:
Orginal list: [18, 81, 45, 76, 33, 54]
Numbers of the above list divisible by nine: [18, 81, 45, 54]

#5 Write a Python program to count the even numbers in a given list of integers 
x= [2,4,3,6,8,7,5,8]
print("Original arrays:",x)
y = len(list(filter(lambda a: (a%2 == 0) , x)))
print("\nNumber of even numbers in the above array: ", y)

OUTPUT:
Original arrays: [2, 4, 3, 6, 8, 7, 5, 8]

Number of even numbers in the above array:5
  
