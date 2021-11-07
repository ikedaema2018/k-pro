inputs = [
    '2 3',
    '1 32',
    '2 63',
    '1 12'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split(' '))

p_y = [list(map(int, input().split(' '))) for _ in range(M)]
enume_p_y = list(enumerate(p_y))
sorted_y = sorted(enume_p_y, key=lambda x: x[1][1])
prefectures = [0] * (N + 1)

conditions = []
for enume_py in sorted_y:
    enume = enume_py[0]
    pre_y = enume_py[1]
    prefectures[enume_py[1][0]] += 1
    conditions.append([enume, str(pre_y[0]).zfill(6) + str(prefectures[pre_y[0]]).zfill(6)])

sorted_conditions = sorted(conditions, key=lambda x: x[0])
for condition in sorted_conditions:
    print(condition[1])
