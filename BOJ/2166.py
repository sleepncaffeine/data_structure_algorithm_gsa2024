# boj 2166

xs = []
ys = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xs.append(xs[0])
ys.append(ys[0])

l, r = 0, 0
for i in range(n):
    l += xs[i] * ys[i + 1]
    r += xs[i + 1] * ys[i]


print(abs(l - r) / 2)
