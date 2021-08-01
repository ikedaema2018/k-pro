inputs = [
    '1210',
]


def input():
    return inputs.pop(0)


S = input()
s_list = list(S)

for c in reversed(list(s_list)):
    if c == '0':
        s_list = s_list[:-1]
    else:
        break

center = -1
if len(s_list) % 2 != 0:
    center = len(s_list) // 2
flag = True
for c_i in enumerate(s_list):
    if c_i[0] == center:
        break
    else:
        if c_i[1] != s_list[len(s_list) - c_i[0] - 1]:
            flag = False

if flag:
    print('Yes')
else:
    print('No')
