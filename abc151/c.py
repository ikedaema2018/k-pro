inputs = [
    '6 0'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split(' '))
result_ac = 0
result_penalty = 0

ac_l = [0] * (N + 1)
pena_l = [0] * (N + 1)

for _ in range(M):
    s_n, answer = input().split(' ')
    n = int(s_n)
    if answer == 'AC' and ac_l[n] == 0:
        ac_l[n] = 1
        result_ac += 1
        result_penalty += pena_l[n]
    if answer == 'WA':
        pena_l[n] += 1

print(f"{result_ac} {result_penalty}")
