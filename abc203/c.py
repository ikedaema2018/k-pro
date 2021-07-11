inputs = [
    '3 2',
    '5 5',
    '2 1',
    '2 2'
]

def input():
    return inputs.pop(0)


N, K = list(map(int, input().split()))

remain = K
current = 0

flag = False
conditions = [list(map(int, input().split())) for _ in range(N)]
conditions = sorted(conditions, key=lambda vv: vv[0])

for condition in conditions:
    A, B = condition
    distance = A - current
    if distance > remain:
        current = current + remain
        remain = 0
        flag = True
        break
    else:
        current = A
        remain = remain - distance + B
print(current + remain)
