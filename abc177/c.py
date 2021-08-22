inputs = [
    '4',
    '141421356 17320508 22360679 244949'
]


def input():
    return inputs.pop(0)


import itertools
N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

ruisekiwa = list(itertools.accumulate(A))
ans = 0
for i in range(len(A)):
    ans += A[i] * (ruisekiwa[-1] - ruisekiwa[i])
print(ans % mod)
