inputs = [
    '5',
    '2 1 5 4 3'
]


def input():
    return inputs.pop(0)

N = int(input())
A = list(map(int, input().split(' ')))

current = A[0]
ans = 0
for a in A[1:]:
    if a < current:
        fumidai = (current - a)
        ans += fumidai
    else:
        current = a
print(ans)
