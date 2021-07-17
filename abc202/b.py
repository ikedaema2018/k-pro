inputs = [
    '0601889'
]

def input():
    return inputs.pop(0)

S = list(reversed(list(input())))
for i in range(len(S)):
    s = S[i]
    if s == '6':
        S[i] = '9'
    elif s == '9':
        S[i] = '6'

print("".join(S))
