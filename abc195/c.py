inputs = [
    '27182818284590',
]


def input():
    return inputs.pop(0)


N = int(input())
count = 0
if N >= 1000:
    count += (N - 999)
if N >= 1000000:
    count += (N - 999999)
if N >= 1000000000:
    count += (N - 999999999)
if N >= 1000000000000:
    count += (N - 999999999999)
if N >= 1000000000000000:
    count += (N - 999999999999999)
print(count)
