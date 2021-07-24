inputs = [
    '6',
    '123 223 123 523 200 2000'
]


def input():
    return inputs.pop(0)


import math
import collections

N = int(input())
items = list(map(int, input().split()))
conditions = list(map(lambda x: x % 200, items))
conditions_count = collections.Counter(conditions)

def count_combination(n):
    if n <= 1:
        return 0
    return math.factorial(n) // (math.factorial(n - 2) * math.factorial(2))

result = 0
for i in list(conditions_count.values()):
    result += count_combination(i)
print(result)