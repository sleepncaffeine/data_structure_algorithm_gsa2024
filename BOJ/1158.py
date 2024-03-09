# boj 1158

n, k = map(int, input().split())
s = list(range(1, n + 1))
res = list()

idx = 0
for i in range(n):
    idx = (idx + k - 1) % len(s)
    res.append(str(s.pop(idx)))

print("<", ", ".join(res), ">", sep="")
