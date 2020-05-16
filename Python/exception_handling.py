a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

"""What if the user gave the second input as a zero, then an error
 will occur, so to handle the error and continue 
 the flow of the execution, we'll block"""


try:
  print("resource open")
  print(a/b)
  k = int(input("Enter vakue: "))
  print(k)
  
#Here except block will handle the error
 
except ZeroDivisionError as e:
  print("Do not divide bt zero")
  
except ValueError as e:
  print("Invalid Inout")
  
except Exception as e:
  print("Something went wrong......")
  
 #Finally block will execute if there is an error or not
  
finally:
  print("resource closed")


print("OK BYE")


