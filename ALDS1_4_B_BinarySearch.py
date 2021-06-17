import math
inputs = [
    '20',
    '0 0 0 1 1 2 2 3 3 3 3 5 6 6 6 8 8 9 9 9',
    '10',
    '9 6 2 4 0 5 1 3 7 8'
]


def input():
    return inputs.pop(0)


n = int(input())
T = list(map(int, input().split()))
q = int(input())
S = list(map(int, input().split()))


first = 0
last = n - 1


flag = True
result = 0

for i in S:
    first = 0
    last = n - 1
    mid = int(math.floor((last + first) / 2))
    while flag:
        print(first, mid, last)
        if first > last:
            break
        if i == T[mid]:
            result += 1
            break
        elif i > T[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = int(math.floor((first + last) / 2))


print(result)
