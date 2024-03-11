# boj 1208


def mid_end(mid, sum):
    if mid == n:
        if sum in sSum:
            sSum[sum] += 1
        else:
            sSum[sum] = 1
        return

    mid_end(mid + 1, sum)
    mid_end(mid + 1, sum + num[mid])


def st_mid(st, sum):
    global cnt
    if st == n // 2:
        if s - sum in sSum:
            cnt += sSum[s - sum]
        return

    st_mid(st + 1, sum)
    st_mid(st + 1, sum + num[st])


n, s = map(int, input().split())
num = list(map(int, input().split()))

sSum = {}
cnt = 0

mid_end(n // 2, 0)
st_mid(0, 0)

if s:
    print(cnt)
else:
    print(cnt - 1)
