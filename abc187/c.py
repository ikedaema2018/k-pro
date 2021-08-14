inputs = [
    '6',
    'a',
    '!a',
    'b',
    '!c',
    'd',
    '!d'
]


def input():
    return inputs.pop(0)

N = int(input())
_S = [input() for _ in range(N)]
S = sorted(_S)
# print(S)

for i in range(N):
    # if i != 3:
    #     continue
    flag = False
    left = 0
    right = len(S) - 1
    target = '!' + S[i]
    # print('!!!!!!!!!!!!!')
    # print(target)
    while left <= right and not flag:
        mid = (right + left) // 2
        mid_v = S[mid]
        if mid_v > target:
            # print('mid_v > target')
            # print(mid)
            # print(target)
            # print(mid_v)
            right = mid - 1
            continue
        if mid_v < target:
            # print('mid_v < target')
            # print(mid)
            # print(target)
            # print(mid_v)
            left = mid + 1
            continue
        flag = True
    if flag:
        print(S[i])
        break
else:
    print('satisfiable')

