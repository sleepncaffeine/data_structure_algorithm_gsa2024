def knapsack_bf(w, v, c):
    n = len(w)
    best = 0

    for i in range(2**n):
        s = [0] * n
        for j in range(n):
            s[j] = i % 2
            i //= 2

        sumv = 0
        sumw = 0
        for j in range(n):
            if s[j] == 1:
                sumv += v[j]
                sumw += w[j]

        if sumw <= c and sumv > best:
            best = sumv

    return best


weights = [10, 20, 30, 25, 35]
values = [60, 100, 120, 70, 85]

print(knapsack_bf(weights, values, 80))


def knapsack_frac(w, v, c):
    best = 0
    for i in range(len(w)):
        if c <= 0:
            break
        if w[i] <= c:
            best += v[i]
            c -= w[i]
        else:
            fraction = c / w[i]
            best += v[i] * fraction
            break
    return best


print(knapsack_frac(weights, values, 80))
