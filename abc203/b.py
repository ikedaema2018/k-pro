inputs = [
    '3 3'
]

def input():
    return inputs.pop(0)


N, K = list(map(int, input().split()))
conditions = []
for n in range(1, N + 1):
    for k in range(1, K + 1):
        conditions.append(f"{n}0{k}")

print(sum(map(int, conditions)))