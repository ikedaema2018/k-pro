inputs = [
    '5',
    '-5 8 9 -4 -3'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1

sum = 0
for i in range(len(d.items())):
    for j in range(i + 1, len(d.items())):
        list_items = list(d.items())
        x = list_items[i]
        y = list_items[j]
        v = (x[0] - y[0]) ** 2
        sum += (v * (x[1] * y[1]))

print(sum)
