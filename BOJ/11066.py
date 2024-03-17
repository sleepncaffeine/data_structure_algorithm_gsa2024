# boj 11066

import sys

input = sys.stdin.readline

INF = 987654321

t = int(input())

for _ in range(t):
    n = int(input())
    size = list(map(int, input().split()))
    s = [0] * (n + 1)
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n + 1):
        s[i] = s[i - 1] + size[i - 1]

    for i in range(1, n):
        for j in range(n - i):
            x, y = j, i + j

            dp[x][y] = INF

            for k in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][k] + dp[k + 1][y])

            dp[x][y] += s[y + 1] - s[x]

    print(dp[0][n - 1])
