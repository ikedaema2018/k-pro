inputs = [
    '2',
    '1 4 2 5'
]


def input():
    return inputs.pop(0)

# 集団を２つに分ける
# 分けた中でそれぞれ一番大きい物を見つける
# ２つを比較して小さい方を出力
N = int(input())
A = list(map(int, input().split(' ')))

a = 0
n = 2 ** N
for _a in A[:n//2]:
    a = max(a, _a)

b = 0
for _b in A[n//2:]:
    b = max(b, _b)

print(A.index(min(a, b)) + 1)
