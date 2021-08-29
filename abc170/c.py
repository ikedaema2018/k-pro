inputs = [
    '9 10',
    '1 5 6 7 8 9 10 11 12 13'
]


def input():
    return inputs.pop(0)


X, N = map(int, input().split())
_P = sorted(list(map(int, input().split())))


def match(A, target):
    low = 0
    high = len(A) - 1
    while high >= low:
        mid = (high + low) // 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1




P = [-1, 101]
for i in range(0, 100 + 1):
    m = match(_P, i)
    if match(_P, i) == -1:
        P.append(i)
P = sorted(P)

ans = 100
sa = 100
for p in P:
    _sa = abs(p - X)
    if _sa < sa:
        ans = p
        sa = _sa

print(ans)
