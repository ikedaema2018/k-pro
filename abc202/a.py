inputs = [
    '1 4 3'
]

def input():
    return inputs.pop(0)

a, b, c = list(map(int, input().split()))
print((7 - a) + (7 - b) + (7 - c))