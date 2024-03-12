# boj 1069

import math
import sys

input = sys.stdin.readline

x, y, d, t = map(int, input().split())

dist = math.sqrt(x**2 + y**2)

if dist >= d:
    print(min(dist, dist // d * t + dist % d, (dist // d + 1) * t))
else:
    print(min(dist, t + d - dist, 2 * t))
