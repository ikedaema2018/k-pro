inputs = [
    '2119'
]


def input():
    return inputs.pop(0)


S = input()
ans = 0
for i in range(0, len(S) - 3):
    for j in range(i + 4, len(S) + 1):
        if int(S[i:j]) % 2019 == 0:
            ans += 1
print(ans)