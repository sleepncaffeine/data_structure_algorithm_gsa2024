# boj 1522

s = input()
ans = 123456789
cnt = s.count("a")

s += s[0:cnt]

for i in range(len(s) - cnt):
    ans = min(ans, s[i : i + cnt].count("b"))

print(ans)
