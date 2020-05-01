succeful=True
while succeful:
  try:
    weight=int(input('\nEnter your weight: '))
    unit=input("in lbs(L) or kg(K): ")
    succeful=False
    if unit.upper()=='L':
      converted=weight*0.45
      print(f"you are {converted} kilos")
      succeful=True
    elif unit.upper()=='K':
      converted=weight/0.45
      print(f"you are {converted} pounds")
      succeful=True
    else:
      print("Put a defined unit ")
      succeful=True
  except ValueError:
    print("Invalid input")
  
