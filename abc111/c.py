inputs = [
    '6',
    '105 119 105 119 105 119'
]


def input():
    return inputs.pop(0)


N = int(input())
V = list(map(int, input().split(' ')))

even = {}
odd = {}

for i in range(len(V)):
    v = V[i]
    if i % 2 == 0:
        even[str(v)] = even[str(v)] + 1 if str(v) in even else 1
    else:
        odd[str(v)] = odd[str(v)] + 1 if str(v) in odd else 1

sorted_even = sorted(even.items(), reverse=True, key=lambda x: x[1])
sorted_odd = sorted(odd.items(), reverse=True, key=lambda x: x[1])

even_1 = [sorted_even[0][0], sorted_even[0][1]]
even_2 = [sorted_even[1][0], sorted_even[1][1]] if len(sorted_even) > 1 else [0, 0]

odd_1 = [sorted_odd[0][0], sorted_odd[0][1]]
odd_2 = [sorted_odd[1][0], sorted_odd[1][1]] if len(sorted_odd) > 1 else [0, 0]

sin_ev = 0
sin_od = 0
if even_1[1] - even_2[1] >= odd_1[1] - odd_2[1]:
    sin_ev = even_1[1]
    if even_1[0] == odd_1[0]:
        sin_od = odd_2[1]
    else:
        sin_od = odd_1[1]
else:
    sin_od = odd_1[1]
    if odd_1[0] == even_1[0]:
        sin_ev = even_2[1]
    else:
        sin_ev = even_1[1]

print(N - sin_ev - sin_od)
