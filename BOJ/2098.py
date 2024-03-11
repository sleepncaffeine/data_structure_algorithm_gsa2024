# boj 2098

INF = 987654321


def dfs(pre, bit, n, dp, mat):
    if bit == (1 << n) - 1:
        if mat[pre][0]:
            return mat[pre][0]
        else:
            return INF

    if dp[pre][bit] != -1:
        return dp[pre][bit]

    dp[pre][bit] = INF

    for i in range(n):
        if not bit & (1 << i):
            if mat[pre][i] != 0:
                dp[pre][bit] = min(
                    dp[pre][bit], dfs(i, bit | (1 << i), n, dp, mat) + mat[pre][i]
                )

    return dp[pre][bit]


n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

print(dfs(0, 1, n, dp, mat))
