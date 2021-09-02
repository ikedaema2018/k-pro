inputs = [
    '4',
    'aaaa',
    'a',
    'aaa',
    'aa'
]


def input():
    return inputs.pop(0)


print(len(set([input() for _ in range(int(input()))])))


