# boj 1966

import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    index = deque(range(n))
    cnt = 0

    while True:
        if q[0] == max(q):
            cnt += 1
            if index[0] == m:
                print(cnt)
                break
            else:
                q.popleft()
                index.popleft()
        else:
            q.append(q.popleft())
            index.append(index.popleft())
