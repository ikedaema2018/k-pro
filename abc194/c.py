inputs = [
    '5',
    '-5 8 9 -4 -3'
]


def input():
    return inputs.pop(0)


import itertools
N = int(input())
items = list(map(int, input().split()))
count = 0
for condition in itertools.combinations(items, 2):
    count += ((condition[0] - condition[1]) ** 2)

print(count)

