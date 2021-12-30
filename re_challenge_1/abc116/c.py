inputs = [
    '8',
    '4 23 75 0 23 96 50 100'
]


def input():
    return inputs.pop(0)


N = int(input())
H = list(map(int, input().split()))

ans = 0
while True:
    flag = False
    break_flag = False
    for i in range(N):
        if H[i] > 0:
            break_flag = True
            H[i] = H[i] - 1
            if not flag:
                ans = ans + 1
                flag = True
        elif flag:
            if H[i] == 0:
                flag = False
    if not break_flag:
        break
print(ans)
