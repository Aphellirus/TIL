list_ = [y for y in range(10) if y%2==0]
filter_ = list(filter(lambda x: x%2==0, range(10)))
a = True

if list_ == filter_:
    print(a)
else:
    print(not a)
