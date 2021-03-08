def bubble(arr):
    for i in range(len(arr) - 1):
        swapped = False
        while not swapped:
            swapped = True
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = False
    return arr

arr = [8, 3, 2, 5, 7] 
arr = bubble(arr)
print(arr)
