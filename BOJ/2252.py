# boj 2252

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
ans = []
heap = deque()

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heap.append(i)

while heap:
    cur = heap.popleft()
    ans.append(cur)

    for n in g[cur]:
        indegree[n] -= 1
        if indegree[n] == 0:
            heap.append(n)

print(*ans)
