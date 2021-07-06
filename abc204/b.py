inputs = [
    '3',
    '6 17 28'
]

def input():
    return inputs.pop(0)

N = input()
fruits = list(map(int, input().split()))

result = 0
for fruit in fruits:
    if fruit > 10:
        result += (fruit - 10)

print(result)