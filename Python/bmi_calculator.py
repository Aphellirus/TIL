print("This program calculates your body mass index")

print("# # # # # # # # # # # # # # # # # # # # # ")

height= float(input())
weight= float(input())
print("What is your height in Meters (e.g=1.65m) : ",height)
print("What is your weight in Kgs (e.g=65.5Kgs) :",weight)
BMI = weight/(height * height)
print()
print()

print("You BMI is:", round(BMI, 2))

if BMI <=18.5:
  BodyStatus = "Underweight"
elif BMI >=18.5 and BMI <=24.9:
  BodyStatus ="Normal weight"
elif BMI >=24.9 and BMI  ==29.9:
  BodyStatus="Overweight"
 
else:
  BodyStatus ="Obesity"
 
print("Your Body Status  is:",BodyStatus)
