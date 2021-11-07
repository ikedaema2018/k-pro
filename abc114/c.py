inputs = [
    '3600'
]


def input():
    return inputs.pop(0)


_N = input()
keta = len(list(_N))
N = int(_N)

if N < 357:
    print(0)
    exit(0)

result = 0

def dfs(selected, gc):
    global result
    if gc > 0:
        n = int("".join(selected))
        if n <= N:
            if not ('3' not in selected or '5' not in selected or '7' not in selected):
                result += 1
        if gc == keta:
            return
    dfs(selected + ['3'], gc + 1)
    dfs(selected + ['5'], gc + 1)
    dfs(selected + ['7'], gc + 1)

dfs([], 0)
print(result)


