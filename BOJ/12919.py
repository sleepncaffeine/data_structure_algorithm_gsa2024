# boj 12919


def solve(t):
    if len(t) == 0:
        return
    if t == s:
        print(1)
        exit()

    if t[-1] == "A":
        solve(t[:-1])
    if t[0] == "B":
        solve(t[1:][::-1])


s = list(input())
t = list(input())

solve(t)

print(0)
