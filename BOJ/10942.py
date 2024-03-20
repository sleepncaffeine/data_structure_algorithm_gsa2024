# boj 10942

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for i in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0

for l in range(n - 2):
    for i in range(n - l - 2):
        j = i + l + 2
        if nums[i] == nums[j] and dp[i + 1][j - 1]:
            dp[i][j] = 1

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
