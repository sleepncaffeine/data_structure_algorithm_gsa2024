def downheap(i, arr, size):
    while i * 2 <= size:
        k = i * 2
        if k < size and arr[k] < arr[k + 1]:
            k += 1
        if arr[i] >= arr[k]:
            break
        arr[i], arr[k] = arr[k], arr[i]
        i = k


def create_heap(arr):
    hsize = len(arr) - 1
    for i in reversed(range(1, hsize // 2 + 1)):
        downheap(i, arr, hsize)


def heap_sort(arr):
    n = len(arr) - 1
    for i in range(n):
        arr[1], arr[n] = arr[n], arr[1]
        downheap(1, arr, n - 1)
        n -= 1


arr = [None, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 21, 31, 22, 44, 17, 20]
print("Before sort:\t", arr[1:])
create_heap(arr)
heap_sort(arr)
print("After sort:\t", arr[1:])
