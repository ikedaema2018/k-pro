inputs = [
    '6',
    '0 153 10 10 23'
]


def input():
    return inputs.pop(0)


N = int(input())
B = list(map(int, input().split(' ')))
result = B[0]

for i in range(len(B)):
    b = B[i]
    if i == (len(B) - 1):
        result += B[i]
    else:
        result += min(B[i], B[i + 1])
print(result)