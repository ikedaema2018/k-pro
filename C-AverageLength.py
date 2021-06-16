from itertools import permutations
import math

inputs = [
    '2',
    '-879 981',
    '-866 890'
]


def input():
    return inputs.pop(0)


N = int(input())
result_distance = 0


coordinates = []
for i in range(N):
    c = list(map(int, input().split()))
    coordinates.append(c)

distance_count = 0

for u in permutations(coordinates, N):
    b_x = None
    b_y = None
    for x, y in u:
        if b_x == None:
            b_x = x
            b_y = y
            continue
        result_distance += ((x - b_x) ** 2 + (y - b_y) ** 2) ** 0.5
        b_x = x
        b_y = y

print(result_distance / (math.factorial(N)))
