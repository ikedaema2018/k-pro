inputs = [
    '2 5',
    '10 12 1 2 14'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split(' '))
titen = map(int, input().split(' '))
D = []
sorted_titen = sorted(titen)

before = None
for t in sorted_titen:
    if before is None:
        before = t
        continue
    else:
        D.append(abs(t - before))
        before = t

sorted_D = sorted(D, reverse=True)
limited_D = sorted_D[N - 1:]
print(sum(limited_D))


