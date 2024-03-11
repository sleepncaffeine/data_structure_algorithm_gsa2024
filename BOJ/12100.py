# boj 12100

from copy import deepcopy


def move(b, d):
    if d == 0:  # NORTH
        for j in range(n):
            lim = 0
            for i in range(1, n):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0

                    if b[lim][j] == 0:
                        b[lim][j] = temp

                    elif b[lim][j] == temp:
                        b[lim][j] = temp * 2
                        lim += 1

                    else:
                        lim += 1
                        b[lim][j] = temp

    elif d == 1:  # EAST
        for i in range(n):
            lim = n - 1
            for j in range(n - 2, -1, -1):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0

                    if b[i][lim] == 0:
                        b[i][lim] = temp

                    elif b[i][lim] == temp:
                        b[i][lim] = temp * 2
                        lim -= 1

                    else:
                        lim -= 1
                        b[i][lim] = temp

    elif d == 2:  # WEST
        for i in range(n):
            lim = 0
            for j in range(1, n):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0

                    if b[i][lim] == 0:
                        b[i][lim] = temp

                    elif b[i][lim] == temp:
                        b[i][lim] = temp * 2
                        lim += 1

                    else:
                        lim += 1
                        b[i][lim] = temp

    else:  # SOUTH
        for j in range(n):
            lim = n - 1
            for i in range(n - 2, -1, -1):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0

                    if b[lim][j] == 0:
                        b[lim][j] = temp

                    elif b[lim][j] == temp:
                        b[lim][j] = temp * 2
                        lim -= 1

                    else:
                        lim -= 1
                        b[lim][j] = temp

    return b


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        dfs(move(deepcopy(board), i), cnt + 1)


ans = 0

n = int(input())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))


dfs(board, 0)

print(ans)
