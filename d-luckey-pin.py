inputs = [
    '19',
    '3141592653589793238'
]


def input():
    return inputs.pop(0)

n = int(input())
s = input()
result = []

for i in range(10):
    i_idx = s.find(str(i))
    if i_idx == -1:
        continue
    for j in range(10):
        j_idx = s.find(str(j), i_idx + 1)
        if j_idx == -1:
            continue
        for k in range(10):
            k_idx = s.find(str(k), j_idx + 1)
            if k_idx == -1:
                continue
            result.append(str(i) + str(j) + str(k))


print(len(set(result)))
