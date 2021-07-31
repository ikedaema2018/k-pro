inputs = [
    '3 3',
    '1 2',
    '2 3',
    '3 1'
]


def input():
    return inputs.pop(0)


N, M = list(map(int, input().split()))
items = [list(map(int, input().split())) for _ in range(M)]
# 辺で繋がれてない点Q個階乗 * 辺で繋がれている点の通り数
