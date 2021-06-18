inputs = [
    # '8',
    # '3',
    # '2',
    # '3',
    # '1',
    # '4',
    # '6'

    '20',
    '4',
    '4',
    '12',
    '8',
    '16',
    '7',
    '7',
    '11',
    '8'
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
d_positions.sort()

deliveries_at = []
for i in range(m):
    deliveries_at.append(int(input()))


def binary_search_delivery_distance(num):
    left = 0
    right = n
    while right - left > 1:
        mid = int((left + right) / 2)
        if num > d_positions[mid]:
            left = mid
        else:
            right = mid
    return min(abs(num - d_positions[right]), abs(num - d_positions[left]))

result = 0
for i in deliveries_at:
    distance = binary_search_delivery_distance(i)
    result += distance

print(result)


