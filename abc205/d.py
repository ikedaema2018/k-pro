from bisect import bisect_right

inputs = [
    '4 3',
    '3 5 6 7',
    '2',
    '5',
    '3'
]


def input():
    return inputs.pop(0)


N, q = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(q):
    t = int(input())
    amount_removed_a = bisect_right(A, t)
    n = 0
    _t = t
    next_a = amount_removed_a
    while n != amount_removed_a and next_a < len(A):
        _t += 1
        if A[next_a] == _t:
            next_a += 1
        else:
            n += 1

    if n != amount_removed_a:
        _t += amount_removed_a - n

    print(_t)

