inputs = [
    '3 4 9 0'
]


def input():
    return inputs.pop(0)


A, B, H, M = map(int, input().split(' '))
deg_h = H * (360 / 12) + (360 / 12) * (M / 60)
deg_m = M * (360 / 60)
deg = abs(deg_h - deg_m)
if deg >= 180:
    deg = 360 - deg
import math
c = math.sqrt(A**2+B**2-2*A*B*math.cos(math.pi * deg / 180))
print(c)
