# boj 5073

while 1:
    ls = list(map(int, input().split()))
    if ls[0] == 0:
        break
    ls.sort()
    if ls[0] + ls[1] <= ls[2]:
        print("Invalid")
    elif ls[0] == ls[1] == ls[2]:
        print("Equilateral")
    elif ls[0] == ls[1] or ls[1] == ls[2]:
        print("Isosceles")
    else:
        print("Scalene")
