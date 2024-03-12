# boj 1197

import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edge = []
ans = 0

for _ in range(e):
    x, y, c = map(int, input().split())
    edge.append((c, x, y))

edge.sort()

for z, x, y in edge:
    if find(x) != find(y):
        union(x, y)
        ans += z

print(ans)
