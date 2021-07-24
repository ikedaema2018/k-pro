inputs = [
    '3',
    '1 5 3',
    '10 7 3'
]


def input():
    return inputs.pop(0)


n = int(input())

low = -1
high = 1e9


A = list(map(int, input().split()))
B = list(map(int, input().split()))

for a in A:
    low = max(low, a)
for b in B:
    high = min(high, b)

print(len(list(range(low, high + 1))))
