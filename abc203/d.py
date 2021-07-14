inputs = [
    '3 3',
    '1 2 3',
    '4 5 6',
    '7 8 9'
]

def input():
    return inputs.pop(0)

N, K = map(int, input().split())
map_depths = []
for _ in range(N):
    map_depths.append(list(map(int, input().split())))

result = []
for i in range(N - K + 1):
    for j in range(N - K + 1):
        rangee = []
        for k in range(K):
            for l in range(K):
                rangee.append(map_depths[i + k][j + l])
        rangee = list(reversed(sorted(rangee)))
        result.append(rangee[(K**2)//2])

print(sorted(result)[0])
