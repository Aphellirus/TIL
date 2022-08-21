# some examples using Random module

import random

x = random.random()
# Random float x, 0.0 <= x < 1.0
print(x)

x = random.uniform(1, 10)  
# Random float x, 1.0 <= x < 10.0
print(x)

x = random.randint(1, 10)  
# Integer from 1 to 10, endpoints included
print(x)

x = random.randrange(0, 101, 2)  
# Even integer from 0 to 100
print(x)

x = random.choice('abcdefghij')  
# Choose a random element
print(x)

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items)


x = random.sample([1, 2, 3, 4, 5],  3)  
# Choose 3 elements
print(x)


print(random.__doc__)
# to know all the doc string under the random module.
