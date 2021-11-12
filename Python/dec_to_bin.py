def decimalToBinary(num):
    binaryNum = [0] * num
    i = 0

    while num > 0:
        binaryNum[i] = (num % 2)
        num = int(num / 2)

        i += 1

    for i in range(i - 1, -1, -1):
        print(binaryNum[i], end = '')

number = input('Enter number: ')
decimalToBinary(int(number))
