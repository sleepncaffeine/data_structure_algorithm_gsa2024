# boj 1202

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split())
gem = []
bag = []

for _ in range(n):
    m, v = map(int, input().split())
    gem.append((m, v))

for _ in range(k):
    bag.append(int(input()))

gem.sort()
bag.sort()

pq = []
ans = 0

for size in bag:
    while gem and gem[0][0] <= size:
        heappush(pq, -gem[0][1])
        heappop(gem)

    if pq:
        ans -= heappop(pq)

print(ans)
