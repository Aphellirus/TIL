from functools import reduce
from operator import mul

n = int(input())
factorial = reduce(mul,[i for i in range(1,n+1)])

print(factorial)
