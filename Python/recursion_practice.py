def apply_five(func, arg : int):

    return [func(func(arg))*i for i in range(0,5)]

def add_five(x):
    return x + 5

'test case'

print(apply_five(add_five, 10))
