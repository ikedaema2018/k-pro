inputs = [
    '999983',
]


def input():
    return inputs.pop(0)


N = int(input())

cur = 0
for i in range(1, 10 ** 7):
    cur *= 10
    cur += 7
    cur %= N
    if cur == 0:
        print(i)
        break
else:
    print('-1')