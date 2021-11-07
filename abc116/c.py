inputs = [
    '8',
    '4 23 75 0 23 96 50 100'
]


def input():
    return inputs.pop(0)

N = int(input())
H = list(map(int, input().split(' ')))
result = 0

while True:
    if max(H) == 0:
        break

    i = 0
    while i < N:
        if H[i] > 0:
            result += 1
            while i < N and H[i] > 0:
                H[i] -= 1
                i += 1
        i += 1

print(result)