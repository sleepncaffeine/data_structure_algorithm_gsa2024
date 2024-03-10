# boj 2292

n = int(input())

r = 1
cnt = 1
while n > r:
    r += 6 * cnt
    cnt += 1

print(cnt)
