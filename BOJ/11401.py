# boj 11401

MOD = 1000000007


def calc(n):
    if n == 0:
        return 1
    if n % 2:
        return calc(n - 1) * y % MOD
    half = calc(n // 2)
    return half * half % MOD


n, k = map(int, input().split())
x, y = 1, 1

for i in range(n, n - k, -1):
    x = x * i % MOD
for i in range(1, k + 1):
    y = y * i % MOD
y = calc(MOD - 2)

print(x * y % MOD)
