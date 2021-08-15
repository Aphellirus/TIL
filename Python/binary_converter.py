def change_to_binary(num):
    binary_format = ""
    while num >= 1:
        sum = int(num % 2)
        if sum == 0:
            binary_format += "0"
        else:
            binary_format += "1"
        num -= num / 2
    return binary_format[::-1]
  
  
print(change_to_binary(167))
