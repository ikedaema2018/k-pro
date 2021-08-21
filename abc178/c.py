inputs = [
    '869121',
]


def input():
    return inputs.pop(0)


N = int(input())
mod = 10**9 + 7
a = pow(10, N, mod)
b = pow(9, N, mod)
c = pow(9, N, mod)
d = pow(8, N, mod)
print((a - b - c + d) % mod)

# ans = pow(10, N, mod)
# ans -= pow(9, N, mod) * 2
# ans += pow(8, N, mod)
# print(ans % mod)
