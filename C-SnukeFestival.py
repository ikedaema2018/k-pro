inputs = [
    '6',
    '3 14 159 2 6 53',
    '58 9 79 323 84 6',
    '2643 383 2 79 50 288'
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
        print(left, right)
    if arr[left] > num:
        while left != 0 and arr[left] == arr[left - 1]:
            left = left - 1
        return left
    elif arr[right] <= num:
        return -1
    else:
        return right

result = 0
for i in range(N):
    target_j = binary_search_min_over_num(a_s[i], b_s)
    if target_j == -1:
        break
    for j in range(target_j, N):
        target_k = binary_search_min_over_num(b_s[j], c_s)
        if target_k == -1:
            break
        for k in range(target_k, N):
            result += 1
print(result)


