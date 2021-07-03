import math
import copy
import sys
inputs = [
    '1',
    '200000'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = list(map(int, input().split()))


def search_kaibun(arr):
    divide = math.floor(len(arr) / 2)
    for i in range(0, divide):
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
    return True


def change(_arr, before_change_char, after_change_char):
    arr = copy.copy(_arr)
    for i in range(len(arr)):
        if arr[i] == before_change_char:
           arr[i] = after_change_char
    return arr


def recursion(arr, pos, count):
    if search_kaibun(arr):
        return count
    if pos >= N:
        return sys.maxsize
    else:
        return min(recursion(arr, pos + 1, count), recursion(change(arr, arr[len(arr) - 1 - pos], arr[pos]), pos + 1, count + 1))

print(recursion(conditions, 0, 0))
