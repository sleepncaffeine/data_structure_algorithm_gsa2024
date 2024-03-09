# boj 9935

import sys

input = sys.stdin.readline

string = input().strip()
boom = input().strip()
l = len(boom)
s = []

for ch in string:
    s.append(ch)
    if ch == boom[-1] and "".join(s[-l:]) == boom:
        del s[-l:]

if s:
    print("".join(s))
else:
    print("FRULA")
