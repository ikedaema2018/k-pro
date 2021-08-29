def match(A, target):
    low = 0
    high = len(A) - 1
    while high >= low:
        mid = (high + low) // 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1