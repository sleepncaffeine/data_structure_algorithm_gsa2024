def mincount(a, k):
    d = [0] * (k + 1)
    for i in range(a + 1, k + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0 and (i // 2) >= a:
            d[i] = min(d[i], d[i // 2] + 1)

    return d[k]


a, k = map(int, input().split())
print(mincount(a, k))


# path
def minpath(a, k):
    d = [0] * (k + 1)
    for i in range(a + 1, k + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0 and (i // 2) >= a:
            d[i] = min(d[i], d[i // 2] + 1)

    path = []
    tmp = k

    while tmp != a:
        path.append(tmp)
        if tmp % 2 == 0 and (tmp // 2) >= a and d[tmp // 2] < d[tmp - 1]:
            tmp = tmp // 2
        else:
            tmp -= 1

    path.append(a)
    path.reverse()
    return path
