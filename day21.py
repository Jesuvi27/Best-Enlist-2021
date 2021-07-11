//1.	Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

la = [1,4,5,6]
lb = [2,8,9,3]
list(zip(la, lb))

OUTPUT:
[(1, 2), (4, 8), (5, 9), (6, 3)]

//2.	First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.

list1=["jeni", "kani", "mayil", "vetri", "reena", "banu", "mano"]
range1 = list(range(1,8))
lst = zip(list1, range1)
print(lst)

OUTPUT:
[('jeni', 1), ('kani', 2), ('mayil', 3), ('vetri', 4), ('reena', 5), ('banu', 6), ('mano', 7)]

//3.	Using sorted() function, sort the list in ascending order.

x = (1,7,5,3,6,2,4)
y = sorted(x)
print(y)

OUTPUT:
[1, 2, 3, 4,5,6,7]

//4.	Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

y = [1,2,3,6,7,8,9,11]
def odd_num(num):
    if(num%2 != 0):
        return True
    else:
        return False

oddNums = filter(odd_num, y)
print('odd Numbers:')
b =[]
for num in oddNums:
    b.append(num)
print(b)

OUTPUT:
odd Numbers:
[1, 3, 7,9,11]
