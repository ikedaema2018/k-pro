inputs = [
    '6',
    'a',
    '!a',
    'b',
    '!c',
    'd',
    '!d'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = []
for _ in range(N):
    conditions.append(input())
conditions = sorted(conditions, key=lambda x: x[1:] + 'a' * 10 if x[0] == '!' else x)

before = conditions[0]
for i in range(1, N):
    condition = conditions[i]
    if condition[0] == '!':
        if condition[1:] == before:
            print(before)
            break
    before = condition
else:
    print('satisfiable')

