#sum of all even and odd number into the given list by user
list=[]
evensum=0
oddsum=0
n=int(input("enter the lenght of list"))
for x in range(n):
  print("enter the number")
  y=input()
  list.append(y)
print(list)
for a in range(n-1,-1,-1):
  b=int(list.pop(a))
  if b%2==0:
    evensum=evensum+b
  else:
    oddsum=oddsum+b
print("sum of even numbers from list is",evensum)
print("sum of odd numbers from list is",oddsum)
