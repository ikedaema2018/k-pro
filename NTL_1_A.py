import math
inputs = [
    '126'
]


def input():
    return inputs.pop(0)


N = int(input())
l = math.floor(math.sqrt(N))
flag = True
_N = N
result = []
while flag and _N != 1:
    for i in range(2, l + 1):
        if _N % i == 0:
            _N = int(_N / i)
            result.append(str(i))
            break
    else:
        flag = False
        result.append(str(_N))
        break

print(f'{N}: {" ".join(result)}')