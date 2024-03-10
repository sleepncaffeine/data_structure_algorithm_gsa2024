# boj 14719

h, w = map(int, input().split())
b = list(map(int, input().split()))
ans = 0

for i in range(1, w - 1):
    l = max(b[:i])
    r = max(b[i + 1 :])
    ans += max(0, min(l, r) - b[i])

print(ans)
