array = [1,2,4,5,7,9,12,24,28,56,87]
n = len(array)

def halfSearch(target, l, r):
    mid = (l + r) // 2
    
    if l >= r and array[mid] != target:
        return False
    print(l,r,mid,array[mid])
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return halfSearch(target, mid + 1, r)
    else:
        return halfSearch(target, l, mid - 1)

        
print(halfSearch(8,0, n - 1))
