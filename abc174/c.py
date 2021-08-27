inputs = [
    '999983'
]


def input():
    return inputs.pop(0)


K = int(input())

amari = 0
for i in range(0, 10 ** 6):
    amari = (amari * 10 + 7) % K
    if amari % K == 0:
        print(i + 1)
        break
else:
    print(-1)
