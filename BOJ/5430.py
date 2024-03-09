# boj 5430

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1].split(",")

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr))

    reverse = False
    error = False
    for cmd in p:
        if cmd == "R":
            reverse = not reverse
        elif cmd == "D":
            if not arr:
                error = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if error:
        print("error")
    else:
        if reverse:
            arr = list(reversed(arr))
        print("[", end="")
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(arr[i], end="")
            else:
                print(arr[i], end=",")
        print("]")
