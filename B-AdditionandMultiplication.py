inputs = [
    10,
    10
]


def input():
    return inputs.pop(0)


N = int(input())
K = int(input())

def recursion(num, count):
    if count == N:
        return num
    return min(recursion(num * 2, count + 1), recursion(num + K, count + 1))


print(recursion(1, 0))


