inputs = [
    '20 3',
    '0 5 15'
]


def input():
    return inputs.pop(0)

K, N = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
most_long_distance = 0
for i in range(len(A) - 1):
    if i == 0:
        most_long_distance = max(most_long_distance, K - A[N - 1] + A[i])
    most_long_distance = max(most_long_distance, A[i + 1] - A[i])

print(K - most_long_distance)
