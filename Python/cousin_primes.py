'''
This code will generate the first 100000 cousin primes.
Cousin primes are prime numbers that differ by 4
'''

from sympy import nextprime, isprime
j = 1 
for _ in range(10000):
  j = nextprime(j)
  if isprime(k := j + 4):
    print((j, k)) #print cousins

