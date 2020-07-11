#Input any number and see a staircase

n=int(input("Enter num:"))
print(n)
m=2
for i in range(n):
   print("*"*(m))
   print("*"*(m))
   m+=2
