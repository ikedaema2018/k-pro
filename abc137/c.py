inputs = [
    '5',
    '1 2 3 4 5'
]


def input():
    return inputs.pop(0)


N = int(input())
H = list(map(int, input().split(' ')))
current = 0
for h in H:
    if current > h:
        print('No')
        break
    current = h - 1 if current != h else h
else:
    print('Yes')
