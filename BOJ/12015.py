import bisect
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

v = []
cnt = 0
check = [0] * n

for i in range(n):
    it = bisect.bisect_left(v, arr[i])
    check[i] = it
    if it == len(v):
        v.append(arr[i])
        cnt += 1
    else:
        v[it] = arr[i]

print(cnt)
