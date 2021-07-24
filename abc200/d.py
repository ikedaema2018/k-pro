inputs = [
    '5',
    '180 186 189 191 218'
]


def input():
    return inputs.pop(0)


N = int(input())
items = list(map(int, input().split()))[:8]
n = len(items)
st = [0] * 200


def output_bitsnum(ns):
    container = []
    for j in range(n):
        if (ns >> j) & 1:
            container.append(j + 1)
    print(len(container), " ".join(map(str, container)))


for i in range(2 ** n):
    sum_n = 0
    condition = []
    for j in range(n):
        if (i >> j) & 1:
            sum_n = (sum_n + items[j]) % 200
    if st[sum_n]:
        print('Yes')
        output_bitsnum(i)
        output_bitsnum(st[sum_n])
        break
    else:
        st[sum_n] = i
else:
    print('No')


