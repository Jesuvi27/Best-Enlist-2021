Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
ANS:
import re
pat="[a-zA-Z0-9]{1}"
x=input("Enter the  string: ")
if(re.search(pat,x)):
    print("String Found")
else:
    print("String Not Found")
 
OUTPUT:
  Enter the  string: Divya
   String Found
  
  Write a Python program that matches a word containing 'ab'.
ANS:  
  import re
pattrn="[\w*a\w*b.\w*]"
x=input("Enter the String :")
if(re.search(pattrn,x)):
    print("String contains ab")
else:
    print("String does not contain ab")
    
OUTPUT:
  Enter the String :abi
  String contains ab
  
Write a Python program to check for a number at the end of a word/sentence.
import re
pattern=r".*[0-9]$"
b=input("Enter the string :")
if(re.search(pattern,b)):
    print("Contains number at the end of the string")
else:
    print("Does not contain number at the end of the string")

  OUTPUT:
    Enter the string :jes3
    Contains number at the end of the string
 
    Enter the string :jes
    Does not contain number at the end of the string
    
  Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
  ANS:
    import re
    x=r"[0-9]{1,3}"
    y=input("Enter the string: ")
    b=re.finditer(x,y)
    for a in b:
     print(a.group(0))
  OUTPUT:
    Enter the string: jes489
    489
    
   Write a Python program to match a string that contains only uppercase letters
 
    ANS:
      import re
      a=input("Enter the String:")
      patterns = '^[A-Z]*$'
      if re.search(patterns, a):
        print("Found ")
      else:
        print("Not Found")
        
        OUTPUT:
          Enter the String:jes
          Not Found
          Enter the String:JES
          Found
    

    
