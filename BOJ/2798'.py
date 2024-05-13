# boj 2798

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
for comb in combinations(cards, 3):
    if sum(comb) <= m and sum(comb) > ans:
        ans = sum(comb)

print(ans)
