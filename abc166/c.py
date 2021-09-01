inputs = [
    '4 3',
    '1 2 3 4',
    '1 3',
    '2 3',
    '2 4'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split())
Hs = list(map(int, input().split()))
Hs.insert(0, 0)
conditions = [list(map(int, input().split())) for _ in range(M)]

tonaris = [[] for _ in range(N + 1)]
for condition in conditions:
    tonaris[condition[0]].append(condition[1])
    tonaris[condition[1]].append(condition[0])
ans = 0
for i in range(1, N + 1):
    if len(tonaris[i]) == 0 or Hs[i] > max(map(lambda x: Hs[x], tonaris[i])):
        ans += 1
print(ans)