import random

p = "paper"
s = "scissors"
r = "rock"

all = p , s , r
Chose = random.choice(all)
print("")
print("-I Chose '" + Chose.upper() + "'..")
print("")

Result = input()
print("..You Chose '" + Result.upper() + "' So:")
print("")

if Result == r and Chose == p:
   print(">>>You Lose!")
   
elif Result == r and Chose == s:
   print(">>>You Win!!")
   
elif Result == p and Chose == r:
   print(">>>You Win!!")
   
elif Result == p and Chose == s:
   print(">>>You Lose!")
   
elif Result == s and Chose == r:
   print(">>>You Lose!")
   
elif Result  == s and Chose == p:
   print(">>>You Win!!")
  
elif Result == Chose:
   print(">>>It's a Draw..")
   
else:
   print(">>>Are You Dumb?")
  
   
