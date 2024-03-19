# boj 9466

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x):
    global cnt
    visited[x] = True
    cycle.append(x)
    num = arr[x]

    if visited[num]:
        if num in cycle:
            cnt += cycle[cycle.index(num) :]
        return

    else:
        dfs(num)


t = int(input())
cnt = []

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(cnt))
    cnt.clear()
