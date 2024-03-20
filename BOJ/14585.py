# boj 14585


def calc(x, y, m):
    if x >= 301 or y >= 301:
        return 0

    ret = dp[x][y]

    if ret != -1:
        return ret

    cnt = max(0, m - x - y) if arr[x][y] else 0
    ret = max(calc(x + 1, y, m), calc(x, y + 1, m)) + cnt
    dp[x][y] = ret

    return ret


dp = [[-1 for _ in range(301)] for _ in range(301)]
arr = [[0 for _ in range(301)] for _ in range(301)]

n, m = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    arr[x][y] = 1

print(calc(0, 0, m))
