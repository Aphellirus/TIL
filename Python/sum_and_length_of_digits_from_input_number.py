# sample input: 7950838994
# sum = 62
#length = 10

n = int(input())
original_input = n

sum = 0
length = 0

while n > 0:
   sum = sum + (n%10)
   n //= 10
   
   length += 1
   
print("The sum of all individual digits in " + str(original_input) + " is: " + str(sum))
print("The number of digits in " + str(original_input) + " is:" + str(length))
