def merge_sort(a, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(a, l, m)
        merge_sort(a, m + 1, r)
        merge(a, l, m, r)


def merge(a, l, m, r):
    k = l
    i = l
    j = m + 1

    while i <= m and j <= r:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
            k += 1
        else:
            temp[k] = a[j]
            j += 1
            k += 1

    if i > m:
        temp[k : k + r - j + 1] = a[j : r + 1]
    else:
        temp[k : k + m - i + 1] = a[i : m + 1]

    a[l : r + 1] = temp[l : r + 1]


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
temp = [0] * len(data)

print("Before sort:", data)
merge_sort(data, 0, len(data) - 1)
print("After sort:", data)
