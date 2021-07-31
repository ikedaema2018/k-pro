inputs = [
    '8 9',
    '0 1 2',
    '0 3 2',
    '1 1 3',
    '1 1 4',
    '0 2 4',
    '1 4 1',
    '0 4 2',
    '0 0 0',
    '1 0 0'
]


def input():
    return inputs.pop(0)


class UnionFind:
    parents = []

    def __init__(self, n):
        for i in range(n + 1):
            self.parents.append(i)

    def root(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.parents[rx] = ry

    def same(self, x, y):
        return self.root(x) == self.root(y)


N, Q = map(int, input().split())
union_find = UnionFind(N)

for _ in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        union_find.unite(a, b)
    else:
        if union_find.same(a, b):
            print('Yes')
        else:
            print('No')

