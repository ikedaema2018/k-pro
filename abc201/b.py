inputs = [
    '4',
    'Kita 3193',
    'Aino 3189',
    'Fuji 3776',
    'Okuhotaka 3190'
]

def input():
    return inputs.pop(0)


N = int(input())
items = [input().split() for _ in range(N)]
sorted_items_desc = sorted(items, key=lambda x: int(x[1]), reverse=True)
print(sorted_items_desc[1][0])