inputs = [
    '1000000',
]


def input():
    return inputs.pop(0)


N = int(input())
ans = 0
for a in range(1, N):
    b_rest = (N - 1) // a
    ans += b_rest
print(ans)
