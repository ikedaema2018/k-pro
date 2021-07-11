inputs = [
    '2 5 2'
]

def input():
    return inputs.pop(0)

a, b, c = list(map(int, input().split()))
if a == b:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)
else:
    print(0)
