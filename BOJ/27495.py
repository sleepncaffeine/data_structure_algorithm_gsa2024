# boj 27495

mdrt = []
sub = []

for _ in range(9):
    mdrt.append(list(input().split()))


for i in range(1, 9, 3):
    for j in range(1, 9, 3):
        if i != 4 or j != 4:
            sub.append([mdrt[i][j], i, j])

sub.sort()

for i in range(8):
    goal = sub[i][0]
    q = sub[i][1]
    p = sub[i][2]

    print(f"#{i + 1}. {goal}")

    spcf_goal = []

    for j in range(q - 1, q + 2):
        for k in range(p - 1, p + 2):
            if k != p or j != q:
                spcf_goal.append([mdrt[j][k], j, k])

    spcf_goal.sort()

    for j in range(8):
        print(f"#{i + 1}-{j + 1}. {spcf_goal[j][0]}")
