inputs = [
    '8'
]


def input():
    return inputs.pop(0)


N = int(input())
ans = 0
limit = int((pow(N, 0.5)))
s = set()
for i in range(2, limit + 1):
    for j in range(2, N):
        t = i ** j
        if t > N:
            break
        s.add(t)
print(N - len(s))