inputs = [
    '2 2'
]


def input():
    return inputs.pop(0)


A, B = map(int, input().split(' '))


result = -1
for i in range(10000,-1,-1):
    _a = i * 8 // 100
    _b = i * 10 // 100
    if A == _a and B == _b:
        result = i
print(result)