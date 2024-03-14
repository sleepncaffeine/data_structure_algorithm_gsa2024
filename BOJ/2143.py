# boj 2143

import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_d = dict()
b_d = dict()

for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s in a_d:
            a_d[s] += 1
        else:
            a_d[s] = 1

for i in range(m):
    s = 0
    for j in range(i, m):
        s += b[j]
        if s in b_d:
            b_d[s] += 1
        else:
            b_d[s] = 1

ans = 0

for key in a_d:
    if t - key in b_d:
        ans += a_d[key] * b_d[t - key]

print(ans)
