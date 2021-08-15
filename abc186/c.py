inputs = [
    '20'
]


def input():
    return inputs.pop(0)


N = int(input())
ans = N

for i in range(1, N + 1):
    s_10 = str(i)
    s_8 = oct(i)
    flag = False
    for s in list(s_10):
        if s == '7':
            flag = True
            ans -= 1
            break
    for s in list(s_8):
        if flag:
            break
        if s == '7':
            flag = True
            ans -= 1

print(ans)

