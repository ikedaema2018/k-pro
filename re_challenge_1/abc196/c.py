inputs = [
    '1333'
]


def input():
    return inputs.pop(0)


N_s = input()
N = int(N_s)
result = 0
for i in range(1, len(N_s) // 2 + 1):
    for j in range(10 ** (i - 1), 10 ** i):
        gattai_j = int(str(j) + str(j))
        if N < gattai_j:
            break
        result += 1
print(result)
