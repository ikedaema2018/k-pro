inputs = [
    '3 0',
    '1000000000 1000000000 1000000000'
]


def input():
    return inputs.pop(0)

N, K = map(int, input().split(' '))
H = list(map(int, input().split(' ')))
sorted_h = sorted(H, reverse=True)
removed_sorted_h = sorted_h[K:]
print(sum(removed_sorted_h))