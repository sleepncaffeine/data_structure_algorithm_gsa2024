# boj 20055

n, k = map(int, input().split())
belt = list(map(int, input().split()))

rob = [0] * n

cnt = 0

while belt.count(0) < k:
    cnt += 1

    belt = [belt[-1]] + belt[:-1]
    rob = [0] + rob[:-1]

    rob[-1] = 0

    for i in range(n - 2, -1, -1):
        if rob[i] and not rob[i + 1] and belt[i + 1]:
            rob[i + 1] = 1
            rob[i] = 0
            belt[i + 1] -= 1

    if not rob[0] and belt[0]:
        rob[0] = 1
        belt[0] -= 1

print(cnt)
