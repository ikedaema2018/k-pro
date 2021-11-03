inputs = [
    '5 2',
    '3 1 2 5',
    '2 2 3',
    '1 0'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split(' '))
conditions = [list(map(int, input().split(' '))) for _ in range(M)]
P = list(map(int, input().split(' ')))

result = 0
for bit in range(2 ** N):  # switch
    switchs = [False] * N
    for j in range(N):
        if bit >> j & 1:
            switchs[j] = True
    for k in range(len(conditions)):
        condition = conditions[k]
        light_on = 0
        for c in condition[1:]:
            s = c - 1
            if switchs[s]:
                light_on += 1
        if light_on % 2 != P[k]:
           break
    else:
        result += 1
print(result)
