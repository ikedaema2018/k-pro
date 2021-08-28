inputs = [
    '18278',
]


def input():
    return inputs.pop(0)


N = int(input())
ans = []
while N != 0:
    N -= 1
    t = N % 26
    cr = chr(97 + t)
    N //= 26
    ans.insert(0, cr)
print("".join(ans))