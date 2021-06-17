1)Write a Python script to merge two Python dictionaries

Ans:
  a={"apple":"orange","red":"orange"}
  b={"grapes":"banana","voilet":"yellow"}
  c=a|b
  print(c)
  
  OUTPUT:
    {'apple': 'orange', 'red': 'orange', 'grapes': 'banana', 'voilet': 'yellow'}

2)Write a Python program to remove a key from a dictionary 
Ans: 
  name = {"kalai":"21","kayal":"17","maran":"22"}
  removed_value = name.pop('kayal') 
  print ("The dictionary after remove is : " + str(name))
  print ("The removed key's value is : " + str(removed_value))
  
  OUTPUT:
    The dictionary after remove is : {'kalai': '21', 'maran': '22'}
The removed key's value is : 17

3)Write a Python program to map two lists into a dictionary

Ans:

Name = ['Kalai','Kayal','Maran'] 
Num = ['24','17','22'] 
Data = dict(zip(Name,Num)) 
print(Data)

OUTPUT:
  {'Kalai': '24', 'Kayal': '17', 'Maran': '22'}

4)Write a Python program to find the length of a set
Ans:
  fruits={"apple","orange","grapes","kiwi"} 
  print(len(fruits))

  OUTPUT:
    4
    
5)Write a Python program to remove the intersection of a 2nd set from the 1st set 
Ans: 
  a={5,3,2,4,1} 
  b={4,3,1,2,6} 
  print(a-b)
  
  OUTPUT:
    {5}
