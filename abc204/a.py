inputs = [
    '0 1',
]

def input():
    return inputs.pop(0)


x, y = input().split()
if x == y:
    print(x)
else:
    ints = ['0', '1', '2']
    ints.remove(x)
    ints.remove(y)
    print(ints[0])

