# boj 1766

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
heap = []
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heap.append(i)

while heap:
    heap.sort()
    cur = heap.pop(0)
    ans.append(cur)

    for n in g[cur]:
        indegree[n] -= 1
        if indegree[n] == 0:
            heap.append(n)

print(*ans)
