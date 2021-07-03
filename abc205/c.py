inputs = [
    '-8 6 3'
]


def input():
    return inputs.pop(0)


def giji_pow(x, y):
    if y % 2 == 0:
        return abs(x)
    else:
        return x


A, B, C = list(map(int, input().split()))
a_c = giji_pow(A, C)
b_c = giji_pow(B, C)
if a_c < b_c:
    print("<")
elif a_c > b_c:
    print(">")
else:
    print("=")
