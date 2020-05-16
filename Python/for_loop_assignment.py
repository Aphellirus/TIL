x=range(20)
for y in x:
    if y%2==0:
        print(y)
print("------------")        
m=range(30,50)
for x in m:
    if x%2==1:
        print(x)
print("------------")
n = range(100,200)
for x in n:
    if x%7==0:
        print("{} is divisible by 7".format(x))
print("--------") 
n = range(0,20)
for x in n:
    if x%2==0:
        print("{} Fizz".format(x)) 
    elif x%3==0:
         print("{} Buzz".format(x))
    else:
         print("{} FizzBuzz".format(x))
            
    
    
        
        
        
