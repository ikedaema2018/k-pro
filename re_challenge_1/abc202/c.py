inputs = [
    '3',
    '2 3 3',
    '1 3 3',
    '1 1 1'
]


def input():
    return inputs.pop(0)

N = int(input())
A = list(map(int, input().split(' ')))
# A[i]と比較するB[C[j]]の数字をkeyに、添字からCの値を逆算するために値にindexの配列を格納

_B = list(map(int, input().split(' ')))
# Bのindexと同じ値を算出するために、C[値] = 該当の値が出てくる回数にする
C = {}
for i in list(map(int, input().split(' '))):
    C[i] = C[i] + 1 if i in C else 1

# Bと一致するCの数を計算しておく
B = {}
for i in range(1, len(_B) + 1):
    in_C_count = C[i] if i in C else 0
    if _B[i - 1] in B:
        B[_B[i - 1]] += in_C_count
    else:
        B[_B[i - 1]] = in_C_count

result = 0
for a in A:
    result += (B[a] if a in B else 0)


print(result)
