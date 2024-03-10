# boj 20437

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())

    d = {}

    for i in range(len(w)):
        if w[i] in d:
            d[w[i]].append(i)
        else:
            d[w[i]] = [i]

    ans = []
    for c in d:
        if len(d[c]) >= k:
            for i in range(len(d[c]) - k + 1):
                ans.append(d[c][i + k - 1] - d[c][i] + 1)

    if len(ans) == 0:
        print(-1)
    else:
        print(min(ans), max(ans))
