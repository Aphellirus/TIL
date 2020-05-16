import random
import numpy as np
while True:
    print("-=-"*15)
    print("    Welcome to the Dice Generator (D&D)")
    print("-=-"*15)
    print('''
    [1] d4
    [2] d6
    [3] d8
    [4] d10
    [5] d12
    [6] d20
    [0] Exit''')
    user = int(input("Choose your dice: "))
    quant = int(input('How many times? '))
    if user == 0:
        break
    elif user == 1:
        for i in range(quant):
            value = np.array(random.randint(1, 4))
            print(f'Dice: {value}')
    elif user == 2:
        for i in range(quant):
            value = int(random.randint(1, 6))
            print(f'Dice: {value}')
    elif user == 3:
        for i in range(quant):
            value =int(random.randint(1, 8))
            print(f'Dice: {value}')
    elif user == 4:
        for i in range(quant):
            value = int(random.randint(1, 10))
            print(f'Dice: {value}')
    elif user == 5:
        for i in range(quant):
            value = int(random.randint(1, 12))
            print(f'Dice: {value}')
    elif user == 6:
        for i in range(quant):
            value = int(random.randint(1, 20))
            print(f'Dice: {value}')
        else:
            print("Unknown option. Try again:")
