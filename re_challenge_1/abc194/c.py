inputs = [
    '3',
    '2 8 4'
]


def input():
    return inputs.pop(0)


from collections import Counter

N = int(input())
A = [*map(int, input().split(' '))]
cnt = Counter(A)

ans = 0
for x in range(-200, 201):
    for y in range(x + 1, 201):
        cx = cnt[x]
        cy = cnt[y]
        a = cx * cy * (x - y) ** 2
        ans += a
print(ans)