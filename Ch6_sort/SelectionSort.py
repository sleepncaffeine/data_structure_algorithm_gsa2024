def selection_sort(a):
    for i in range(0, len(a) - 1):
        mini = i
        for j in range(i, len(a)):
            if a[j] < a[mini]:
                mini = j
        a[i], a[mini] = a[mini], a[i]


arr = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 21, 31, 22, 44, 17, 20]
print("Before sort:\t", arr)
selection_sort(arr)
print("After sort:\t", arr)
