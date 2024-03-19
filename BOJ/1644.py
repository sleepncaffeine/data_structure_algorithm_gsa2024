# boj 1644

n = int(input())

# seive
prime = [True] * (n + 1)
prime[0] = prime[1] = False
for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

prime = [i for i in range(n + 1) if prime[i]]

s, e, cnt, total = 0, 0, 0, 0
while True:
    if total >= n:
        if total == n:
            cnt += 1
        total -= prime[s]
        s += 1
    elif e == len(prime):
        break
    else:
        total += prime[e]
        e += 1
print(cnt)
