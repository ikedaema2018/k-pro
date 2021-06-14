inputs = [
    '5 2',
    '3 1 2 5',
    '2 2 3',
    '1 0',
]


def input():
    return inputs.pop(0)


switchNumber, lightBulbNumber = list(map(int, input().split()))

switchesArr = []
for i in range(lightBulbNumber):
    tpm = list(map(int, input().split()))
    switches = tpm[1:]
    switchesArr.append(switches)

litCounts = list(map(int, input().split()))

result = 0
for switches_bit in range(2 ** switchNumber):
    _all = False
    for i in range(len(switchesArr)):
        flag = litCounts[i]
        _count = 0
        for j in range(0, len(switchesArr[i])):
            if (switches_bit >> (switchNumber - switchesArr[i][j])) & 1:
                _count += 1
        if _count % 2 != flag:
            break
        if i == len(switchesArr) - 1:
            _all = True
    if _all:
        result += 1

print(result)
