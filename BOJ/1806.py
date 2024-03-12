# boj 1806

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

st, end = 0, 0
tot = 0
minl = 100001

while True:
    if tot >= s:
        minl = min(minl, end - st)
        tot -= nums[st]
        st += 1
    elif end == n:
        break
    else:
        tot += nums[end]
        end += 1

if minl == 100001:
    print(0)
else:
    print(minl)
