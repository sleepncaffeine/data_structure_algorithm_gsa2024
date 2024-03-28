def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


arr = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 21, 31, 22, 44, 17, 20]
print("Before sort:\t", arr)
insertion_sort(arr)
print("After sort:\t", arr)
