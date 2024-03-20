# boj 26069.py

n = int(input())

rainbow = set(["ChongChong"])

for _ in range(n):
    a, b = input().split()
    if a in rainbow or b in rainbow:
        rainbow.update([a, b])

print(len(rainbow))
