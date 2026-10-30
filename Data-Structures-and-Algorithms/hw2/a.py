t = int(input())
for h in range(t):
    n = int(input())
    s = input().split()
    cur = []
    a = []

    for i in s:
        cur.append(i)
        for j in cur:
            d = cur.count(j)
            if d == 1:
                a.append(j)
                break
        else:
            a.append("-1")

print(*a)
        

