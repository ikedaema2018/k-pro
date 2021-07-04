inputs = [
    '8',
    '1 5 3 2 5 2 3 1'
]


def input():
    return inputs.pop(0)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -(self.parents[x])

N = int(input())
uf = UnionFind(N)
A = list(map(int, input().split()))
for i in range(N // 2):
    if A[i] == A[N - i - 1]:
        continue
    uf.union(i, N - i - 1)

seen = set()
result = 0
for i in range(N):
    root = uf.find(i)
    if root in seen:
        continue
    seen.add(root)
    result += (uf.size(root) - 1)
print(result)