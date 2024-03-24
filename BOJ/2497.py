# boj 2467

n = int(input())
fac = list(map(int, input().split()))

l, r = 0, n - 1

ans = [0, 0]
val = 9876543210

while l < r:
    tmp = fac[l] + fac[r]
    if abs(tmp) < val:
        val = abs(tmp)
        ans = [fac[l], fac[r]]
    if tmp > 0:
        r -= 1
    elif tmp < 0:
        l += 1
    else:
        break

print(*ans)
