inputs = [
    '4',
    'ushi',
    'tapu',
    'nichia',
    'kun'
]


def input():
    return inputs.pop(0)


N = int(input())
S = []

for _ in range(N):
    S.append(input())
S = sorted(S)

result = []
before = S[0]
count = 1
for i in range(1, len(S)):
    s = S[i]
    if before == s:
        count += 1
        continue
    result.append([count, before])
    count = 1
    before = s
else:
    result.append([count, before])


result = sorted(result, key=lambda x: x[0], reverse=True)
before_count = result[0][0]
for c, s in result:
    if before_count != c:
        break
    before_count = c
    print(s)
