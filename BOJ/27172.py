# boj 27172


import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().rstrip().split()))

cards = set(nums)
m = max(nums)
sieve = [0 for _ in range(m + 1)]

for i in nums:
    if i == m:
        continue
    for j in range(2 * i, m + 1, i):
        if j in cards:
            sieve[i] += 1
            sieve[j] -= 1

print(*[sieve[i] for i in nums])
