inputs = [
    '314159265358979323 846264338327950288 419716939 937510582'
]


def input():
    return inputs.pop(0)


A, B, C, D = map(int, input().split(' '))

div_b_c = B // C
div_a_c = (A - 1) // C

div_b_d = B // D
div_a_d = (A - 1) // D

import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


div_b_cd = B // lcm(C, D)
div_a_cd = (A - 1) // lcm(C, D)

print((B - A + 1) - ((div_b_c - div_a_c) + (div_b_d - div_a_d) - (div_b_cd - div_a_cd)))
