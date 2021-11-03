inputs = [
    '0'
]


def input():
    return inputs.pop(0)

l_1 = 0
l_2 = 0
panels = list(map(int, input()))
for i in range(len(panels)):
    panel = panels[i]
    is_odd = i % 2 == 1

    if is_odd:
        if panel == 1:
            l_1 += 1
        else:
            l_2 += 1
    else:
        if panel == 1:
            l_2 += 1
        else:
            l_1 += 1
print(min(l_1, l_2))