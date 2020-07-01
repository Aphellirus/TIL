number_list = []
maxLenghtList = 6
new_list = []

while len(number_list) < maxLenghtList:
  number = input("Enter a new number: ")
  number_list.append(number)
  print ("your last number was: " + str(number))
  if int(number) <= 5:
    new_list.append(number)
  if number == "":
    break
  
  
print ("your list has the numbers:" + str(number_list)) 
print ("all the numbers that are less than 5:" + str(new_list))
