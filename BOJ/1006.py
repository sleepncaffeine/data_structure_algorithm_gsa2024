# boj 1006

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n == 1:
        if a[0] + b[0] <= w:
            print(1)
        else:
            print(2)
        continue

    dp = [[float("inf")] * n for _ in range(3)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[2][0] = 1
    if a[0] + a[-1] <= w:
        dp[0][n - 1] = 1
    if b[0] + b[-1] <= w:
        dp[1][n - 1] = 1
    if a[0] + a[-1] <= w and b[0] + b[-1] <= w:
        dp[2][n - 1] = 2

    for i in range(1, n):
        if a[i] + a[i - 1] <= w:
            dp[0][i] = min(dp[0][i], dp[0][i - 1] + 1)
        else:
            dp[0][i] = min(dp[0][i], dp[0][i - 1] + 2)
        if b[i] + b[i - 1] <= w:
            dp[1][i] = min(dp[1][i], dp[1][i - 1] + 1)
        else:
            dp[1][i] = min(dp[1][i], dp[1][i - 1] + 2)
        if a[i] + a[i - 1] <= w and b[i] + b[i - 1] <= w:
            dp[2][i] = min(dp[2][i], dp[2][i - 1] + 2)
        else:
            dp[2][i] = min(dp[2][i], dp[2][i - 1] + 4)

    for i in range(2, n):
        if a[i] + a[i - 1] <= w:
            dp[0][i] = min(dp[0][i], dp[1][i - 1] + 1)
        if b[i] + b[i - 1] <= w:
            dp[1][i] = min(dp[1][i], dp[0][i - 1] + 1)
        if a[i] + a[i - 1] <= w and b[i] + b[i - 1] <= w:
            dp[2][i] = min(dp[2][i], dp[2][i - 1] + 2)

    print(min(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1]))
