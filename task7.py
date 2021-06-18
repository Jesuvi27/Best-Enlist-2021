1)Create a function getting two integer inputs from user. & print the following:

Addition of two numbers is +value
Subtraction of two numbers is +value
Multiplication of two numbers is +value
Division of two numbers is +value
Here the value represents math function associated

Ans:

print("Input value of x and y") 
x,y =map(int,input().split())
print("The value of x and y are:",x,y) 
sum = x+y
print ("sum:",sum)
sub = x-y 
print ("sub:",sub)
mul = x*y 
print ("mul:",mul)
div = x/y 
print ("div:",div)

OUTPUT:
Input value of x and y
7 8
The value of x and y are: 7 8
sum: 15
sub: -1
mul: 56
div: 0.875

Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree Ans:

def covid(patient_name,body_temperature=98):
print("patient name:",patient_name)
print("patient body temperature:",body_temperature) covid("Jesuvi")

OUTPUT:
patient name: Jesuvi
patient body temperature: 98
