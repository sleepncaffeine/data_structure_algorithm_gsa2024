from math import ceil

h, w, n, m = map(int, input().split())
x = ceil(w / (m + 1))
y = ceil(h / (n + 1))
print(x * y)
