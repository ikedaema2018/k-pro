inputs = [
    '4 5'
]


def input():
    return inputs.pop(0)


L, R = list(map(int, input().split(' ')))
result = 2019

for i in range(L, R):
    for j in range(i + 1, R + 1):
        result = min((i * j) % 2019, result)
        if result == 0:
            break
    if result == 0:
        break

print(result)