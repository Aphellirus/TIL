"""
this program asks the user for a number 
and then prints out a list of all the 
divisors of that number. 
"""



divisors = []
number = int(input("enter a number: ")) 
listRange = list(range(1,number+1)) 

for x in listRange:
  
  if number % x == 0:
    divisors.append(x)
    
    
print (divisors)
  
