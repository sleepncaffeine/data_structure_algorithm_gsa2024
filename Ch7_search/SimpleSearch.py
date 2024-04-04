def sequential_search(A, key, low, high):
    for i in range(low, high):
        if A[i] == key:
            return i
    return -1


def sequential_search_transpose(A, key, low, high):
    for i in range(low, high):
        if A[i] == key:
            if i > low:
                A[i], A[i - 1] = A[i - 1], A[i]
                i -= 1
            return i
    return -1


def binary_search(A, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search(A, key, low, mid - 1)
        else:
            return binary_search(A, key, mid + 1, high)
    return -1


def binary_search_iter(A, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
