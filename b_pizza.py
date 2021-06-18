import sys

inputs = [
    '8',
    '3',
    '2',
    '3',
    '1',
    '4',
    '6'
]

def input():
    return inputs.pop(0)


d = int(input())
n = int(input())
m = int(input())

d_positions = [0]
for i in range(n - 1):
    d_positions.append(int(input()))
d_positions.append(d)

deliveries_at = []
for i in range(m):
    deliveries_at.append(int(input()))

def search_delivery_distance(num):
    most_near = sys.maxsize
    for p in d_positions:
        if abs(p - num) < most_near:
            most_near = abs(p - num)
    return most_near

result = 0
for i in deliveries_at:
    distance = search_delivery_distance(i)
    result += distance

print(result)


