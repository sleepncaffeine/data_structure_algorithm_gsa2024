# boj 11049

import sys

input = sys.stdin.readline
INF = 987654321

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        dp[j][j + i] = INF

        for k in range(j, j + i):
            dp[j][j + i] = min(
                dp[j][j + i],
                dp[j][k] + dp[k + 1][j + i] + arr[j][0] * arr[k][1] * arr[j + i][1],
            )

print(dp[0][n - 1])
