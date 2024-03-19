# boj 1700

n, k = map(int, input().split())
a = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(k):
    if a[i] in plug:
        continue

    if len(plug) < n:
        plug.append(a[i])
        continue

    cnt += 1
    m_idx = 0
    m_val = 0

    for j in range(n):
        if plug[j] in a[i:]:
            idx = a[i:].index(plug[j])
        else:
            idx = 101

        if idx > m_val:
            m_val = idx
            m_idx = j

    plug[m_idx] = a[i]

print(cnt)
