# boj 24479

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(t):
    global ans
    visited[t] = ans
    graph[t].sort()
    for i in graph[t]:
        if not visited[i]:
            ans += 1
            dfs(i)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
ans = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r)
for i in range(1, n + 1):
    print(visited[i])
