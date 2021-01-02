"If the try block executes without entering any exception blocks, then the else block is entered. And then, the finally block is executed"
try:
    a=5/2
except :
    print("Error")
else:
    print("There is no error")
finally:
    print("Happy new year")
