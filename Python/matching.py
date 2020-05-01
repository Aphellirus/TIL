import random
accept=False
count=int(input("Enter number of player to match with each other = ")) 
array=[]
while count != 0:
  if accept ==False:
    t1=raw_input("Enter player name: ")
    array.append(t1)
    count = count - 1
    accept = True
  else:
    t1=raw_input("Enter another name: ")
    array.append(t1)
    count = count - 1

print("\n")
print("the matching is -")

while len(array)>1:
  num1=random.randint(0,len(array)-1)
  num2=random.randint(0,len(array)-1)
  var1=array[num1]
  var2=array[num2]
  if num1!= num2:
    if len(array)==2:
      print(array[0],array[1])
      array.clear()
    else:
      print(var1+" - "+ var2)
      array.remove(var1)
      array.remove(var2)
  
if array != []:
  print('\n')
  print("The person remained unmatched is-")
  print(array[0])
