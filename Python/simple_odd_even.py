#type a number and see whether it's odd or even


number = int(input ("Enter a number: ")) 
  
if number % 2 == 0:
  print ("You number was " + str(number) + ", which is a even number.")
else:
  print ("You number was " + str(number) + ", which is a odd number.") 
