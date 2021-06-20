inputs = [
'6',
'3 14 159 2 6 53',
'58 9 79 323 84 6',
'2643 383 2 79 50 288'
]


def input():
    return inputs.pop(0)


N = input()
a_s = list(map(int, input().split()))
b_s = list(map(int, input().split()))
c_s = list(map(int, input().split()))
a_s.sort()
b_s.sort()
c_s.sort()

result = 0
for i in a_s:
    for j in b_s:
        if i >= j:
            continue
        for k in c_s:
            if j >= k:
                continue
            result += 1
print(result)


