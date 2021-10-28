inputs = [
    '10 7 100',
]


def input():
    return inputs.pop(0)


A, B, X = map(int, input().split(' '))
def buyNPrice(N):
    return A * N + B * len(str(N))


def search():
    low = 1
    high = 10 ** 9

    while low <= high:
        mid = (low + high) // 2
        price = buyNPrice(mid)
        if X > price:
            low = mid + 1
        elif X < price:
            high = mid - 1
        else:
            return mid
    if X > price:
        return mid
    else:
        return mid - 1

print(search())
