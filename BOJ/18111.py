# boj 18111

import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

t_min = float("inf")
h_max = 0

for i in range(257):
    ub = 0
    tb = 0

    for x in range(n):
        for y in range(m):
            if ground[x][y] > i:
                tb += ground[x][y] - i
            else:
                ub += i - ground[x][y]

    if ub > tb + b:
        continue

    count = tb * 2 + ub

    if count <= t_min:
        t_min = count
        h_max = i

print(t_min, h_max)
