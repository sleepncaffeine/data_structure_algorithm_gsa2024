# boj 28018

import sys

input = sys.stdin.readline

n = int(input())

ps = [0] * 1000002

for _ in range(n):
    a, b = map(int, input().split())
    ps[a] += 1
    ps[b + 1] -= 1

for i in range(1, 1000002):
    ps[i] += ps[i - 1]

q = int(input())
query = [int(t) for t in input().split()]

for q in query:
    print(ps[q])
