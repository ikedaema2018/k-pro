inputs = [
    '3',
    '1 1 1',
    '2 2 2',
    '3 3 3'
]


def input():
    return inputs.pop(0)


N = int(input())
a_s = list(map(int, input().split()))
b_s = list(map(int, input().split()))
c_s = list(map(int, input().split()))
a_s.sort()
b_s.sort()
c_s.sort()


def binary_search_min_over_num(num, arr):
    left = 0
    right = len(arr) - 1
    while right - left > 1:
        mid = int((left + right) / 2)
        if num >= arr[mid]:
            left = mid
        else:
            right = mid
    target = None
    if arr[left] > num:
        target = left
    elif arr[right] <= num:
        return -1
    else:
        target = right
    while target != 0 and arr[target] == arr[target - 1]:
        target = target - 1
    return target

def binary_search_min_over_reverse_num(num, arr):
    left = 0
    right = len(arr) - 1
    while right - left > 1:
        mid = int((left + right) / 2)
        if num <= arr[mid]:
            right = mid
        else:
            left = mid
    target = None
    if arr[right] < num:
        target = right
    elif arr[left] >= num:
        return -1
    else:
        target = left
    while target != N - 1 and arr[target] == arr[target + 1]:
        target = target + 1
    return target



result = 0
for b_i in range(N):
    b = b_s[b_i]
    a_i = binary_search_min_over_reverse_num(b, a_s)
    if a_i == -1:
        continue
    c_i = binary_search_min_over_num(b, c_s)
    if c_i == -1:
        continue
    result += (a_i + 1) * (N - c_i)

print(result)

# a = [0,0,0,0,1,1,1,1,2,2,2,2]
# print(binary_search_min_over_num(1,a))
# print(binary_search_min_over_reverse_num(1, a))