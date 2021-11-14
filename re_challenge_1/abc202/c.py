inputs = [
    '3',
    '1 2 2',
    '3 1 2',
    '2 3 2'
]


def input():
    return inputs.pop(0)

N = int(input())
A = list(map(int, input().split(' ')))
# A[i]と比較するB[C[j]]の数字をkeyに、添字からCの値を逆算するために値にindexの配列を格納
B = {}
_B = list(map(int, input().split(' ')))
for i in range(1, len(_B) + 1):
    B[_B[i - 1]] = B[_B[i - 1]] + [i] if _B[i - 1] in B else [i]

# Bのindexと同じ値を算出するために、C[値] = 該当の値が出てくる回数にする
C = {}
for i in list(map(int, input().split(' '))):
    C[i] = C[i] + 1 if i in C else 1

result = 0
for a in A:
    b_idxs = B[a] if a in B else []
    _result = 0
    for i in range(len(b_idxs)):
        _result += C[b_idxs[i]] if b_idxs[i] in C else 0

    result += _result


print(result)
