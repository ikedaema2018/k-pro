inputs = [
    '100128'
]


def input():
    return inputs.pop(0)


N = int(input())
increase = 1
piggy_bank = 0
days = 0
while N > piggy_bank:
    piggy_bank += increase
    increase += 1
    days += 1

print(days)