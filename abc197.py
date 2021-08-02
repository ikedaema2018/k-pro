inputs = [
    '3',
    '1 5 7'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split()))
import sys
m = sys.maxsize
for i in range(2 ** N):
    S = []
    G = []
    for j in range(N):
        if (i >> j) & 1:
            S.append(A[j])
        else:
            G.append(A[j])
    if len(S) <= 0:
        continue
    if len(G) <= 0:
        continue
    s_or = S[0]
    for s_i in range(1, len(S)):
        s_or = s_or | S[s_i]
    g_or = G[0]
    for g_i in range(1, len(G)):
        g_or = g_or | G[g_i]
    m = min(m, (s_or ^ g_or))
print(m)
