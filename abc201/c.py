inputs = [
    'ooo???xxxx'
]


def input():
    return inputs.pop(0)


S = list(input())
exist = []
empty = []
optional = []

for i in range(10):
    if S[i] == 'o':
        exist.append(str(i))
    elif S[i] == 'x':
        empty.append(str(i))
    elif S[i] == '?':
        optional.append(str(i))

def verify(s):
    for e in exist:
        if s.find(str(e)) == -1:
            return False
    possibility = "".join(optional) + "".join(exist)
    for c in list(s):
        if possibility.find(c) == -1:
            return False
    return True


result = 0
for i in range(0, 10000):
    b = verify(str(i).rjust(4, '0'))
    if b:
        result += 1

print(result)


