class Multiply:
    
    def __init__(self, x, y):
        if int != type(x) and int != type(y):
            raise TypeError('%s and %s parameters must be as %s type'%(type(x), type(y), int))
        self.first_integer = x
        self.second_integer = y
        self.result = str(x * y)
        self.steps = [
            str(step) for step in [
                int(_) * x for _ in str(y)[::-1]
            ]
        ]
    @property
    def solution(self):
        sln = [
            *map(
                lambda e: str(e), 
                [
                    self.first_integer, self.second_integer
                ]
            )
        ]
        hr = len(self.result + '__') * '-'
        index = 0
        sln.append(hr)
        for d in sln[ 1 ][::-1]:
            sln.append(
                ' ' * (len(self.result) - len(str(int(d) * int(sln[ 0 ]))) - index)
                + str(int(sln[ 0 ]) * int(d)) 
                + '0' * index
            )
            index += 1
        sln[ 0 ] = (len(self.result[:]) - len(sln[ 0 ])) * ' ' + sln[ 0 ]
        sln[ 1 ] = (len(self.result) - len(sln[ 1 ])) * ' ' + sln[ 1 ]
        sln[ 1 ] = sln[ 1 ] + ' x '
        sln.append(
            sln.pop() + ' + '
        )
        sln.append(hr)
        sln.append(self.result)
        return (
            '\n'.join(
                sln
            )
        )

print(Multiply(123456789, 1367654321).solution)



