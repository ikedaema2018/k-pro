inputs = [
    '2',
]


def input():
    return inputs.pop(0)


import itertools
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_r = list(itertools.accumulate(A))
B_r = list(itertools.accumulate(B))
A_r.insert(0, 0)
B_r.insert(0, 0)

ans = 0
import bisect
for a_i in range(len(A_r)):
    rest = K - A_r[a_i]
    if rest < 0:
        break
    b_i = bisect.bisect_right(B_r, rest)
    books = a_i + b_i - 1
    ans = max(books, ans)
print(ans)