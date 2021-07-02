inputs = [
    '19',
    '4 210068409 221208102',
    '4 16698200 910945203',
    '4 76268400 259148323',
    '4 370943597 566244098',
    '1 428897569 509621647',
    '4 250946752 823720939',
    '1 642505376 868415584',
    '2 619091266 868230936',
    '2 306543999 654038915',
    '4 486033777 715789416',
    '1 527225177 583184546',
    '2 885292456 900938599',
    '3 264004185 486613484',
    '2 345310564 818091848',
    '1 152544274 521564293',
    '4 13819154 555218434',
    '3 507364086 545932412',
    '4 797872271 935850549',
    '2 415488246 685203817'
]


def input():
    return inputs.pop(0)


N = int(input())
l = [0] * N
r = [0] * N
for i in range(N):
    t, l[i], r[i] = list(map(int, input().split()))
    # 疑問がある
    if t == 2:
        r[i] -= 0.5
    elif t == 3:
        l[i] += 0.5
    elif t == 4:
        r[i] -= 0.5
        l[i] += 0.5

result = 0
for i in range(0, N):
    for j in range(i + 1, N):
        result += (min(r[i], r[j]) >= max(l[i], l[j]))

print(result)
