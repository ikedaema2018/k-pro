inputs = [
    '5 12',
    '0 1 4',
    '0 2 3',
    '1 1 2',
    '1 3 4',
    '1 1 4',
    '1 3 2',
    '0 1 3',
    '1 2 4',
    '1 3 0',
    '0 0 4',
    '1 0 2',
    '1 3 0'
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


N, q = list(map(int, input().split()))
union_find = UnionFind(N)

for _ in range(q):
    com, x, y = list(map(int, input().split()))
    if com == 0:
        union_find.union(x, y)
    elif com == 1:
        if union_find.same(x, y):
            print("1")
        else:
            print("0")
