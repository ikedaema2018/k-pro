inputs = [
    '14',
    '99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1'
]


def input():
    return inputs.pop(0)


N = int(input())
D = list(sorted(list(map(int, input().split(' ')))))
div = len(D) // 2
print(D[div] - D[div - 1])
