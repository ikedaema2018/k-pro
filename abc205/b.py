inputs = [
    '5',
    '3 1 2 4 5'
]


def input():
    return inputs.pop(0)


N = int(input())
arr_a = list(map(int, input().split()))
arr_a.sort()
arr_b = [i for i in range(1, N + 1)]

if arr_a == arr_b:
    print("Yes")
else:
    print("No")
