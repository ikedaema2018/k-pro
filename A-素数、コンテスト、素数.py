import math
inputs = [
    '17'
]


def input():
    return inputs.pop(0)


N = int(input())
l = math.floor(math.sqrt(N))
flag = True
for i in range(2, l + 1):
    if N % i == 0:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
