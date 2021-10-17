from functools import reduce
import math

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)