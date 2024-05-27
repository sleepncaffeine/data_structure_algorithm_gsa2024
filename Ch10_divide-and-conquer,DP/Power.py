def slow_power(x, n):
    res = 1.0
    for _ in range(n):
        res *= x
    return res


def power(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)


### compare ###

import time

print("brute-force (2**500) =", slow_power(2, 500))
print("divide-and-conquer (2**500) =", power(2, 500))

t1 = time.time()
for i in range(100000):
    power(2, 500)
t2 = time.time()
for i in range(100000):
    slow_power(2, 500)
t3 = time.time()
print("brute-force (2**500) elapsed time:", t3 - t2)
print("divide-and-conquer (2**500) elapsed time:", t2 - t1)
