a = [1, 3, 5, 4, 2]
def sort(arr)
    a = (arr.min..arr.max).to_a & arr
end
p sort(a)
