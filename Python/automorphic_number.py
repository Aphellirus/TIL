#If the square of a number ends with the        number itself, it is considered to be automorphic.

#Example : 25 is an automorphic number, as the square of 25 = 625 (ends with 25).Sequence of automorphic numbers: 1, 5, 6, 25, 76, 376, ..



print("Checking Automorphic number")
print("____________________________\n")
num = int(input())
if (num**2)%(10**(len(str(num)))) == num:
 print(num,"is an Automorphic number\n\n\n")
else:
 print(num,"is not an Automorphic number\n\n\n")
print("Automorphic number up to 10000")
print("_____________________________\n")
num2 = 10000
for num3 in range(num2):
 if (num3**2)%(10**(len(str(num3)))) == num3:
   print(num3)
