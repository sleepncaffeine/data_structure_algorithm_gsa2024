import collections


def fibo_bf(n):
    if n <= 1:
        return n
    return fibo_bf(n - 1) + fibo_bf(n - 2)


dp_memo = collections.defaultdict(int)


def fibo_memo(n):
    if n <= 1:
        return n
    if dp_memo[n]:
        return dp_memo[n]
    dp_memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
    return dp_memo[n]


dp_tab = collections.defaultdict(int)


def fibo_tab(n):
    dp_tab[0] = 0
    dp_tab[1] = 1
    for i in range(2, n + 1):
        dp_tab[i] = dp_tab[i - 1] + dp_tab[i - 2]
    return dp_tab[n]


print(fibo_bf(10))
print(fibo_memo(10))
print(fibo_tab(10))
