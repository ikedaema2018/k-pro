inputs = [
    '5 2 3 2'
]


def input():
    return inputs.pop(0)


A, B, C, D = list(map(int, input().split()))
result = 0
blue_count = A
red_count = 0
if B >= C * D:
    print(-1)
else:
    while (red_count * D) < blue_count:
        blue_count += B
        red_count += C
        result += 1
    print(result)

