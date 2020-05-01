num1 = int(input("Enter the 1st No."))
num2 = int(input("Enter the 2nd No."))

print("Select Operation")
print(" 1 = add 2 = sub 3 = multi 4 = divi\n")

num = int(input("Enter the Operation\n"))

if num == 1:
  add = num1 + num2
  print("result")
  print(add)

if num == 2:
  sub = num1 - num2
  print("result")
  print(sub)
  
if num == 3:
  multi = num1 * num2
  print("result")
  print(multi)
  
if num == 4:
  divi = num1 % num2
  print("result")
  print(divi)
