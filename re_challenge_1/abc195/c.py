inputs = [
    '1010'
]


def input():
    return inputs.pop(0)


N_s = input()
N = int(N_s)
result = 0

keta = len(N_s)
for i in range(1, keta + 1):
    if i < 4:
        continue
    quantity = 10 ** i - 10 ** (i - 1)
    if i == keta:
        quantity = N - (10 ** (i - 1)) + 1
    result += (quantity * ((i - 1) // 3))
print(result)