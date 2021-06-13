inputs = [
    '12',
    '100 8 5 8 11 13 99 59 51 37 103 40',
    '105',
    '350'
]


def input():
    return inputs.pop(0)


n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for _m in m:
    flag = False
    for i in range(2**len(A)):
        count = 0
        for j in range(len(A)):
            if (i >> j) & 1:
                count += A[j]
        if count == _m:
            flag = True
    if flag:
        print('yes')
    else:
        print('no')
