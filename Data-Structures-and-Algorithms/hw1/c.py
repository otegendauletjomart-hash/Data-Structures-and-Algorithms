a = int(input())

if a < 2:
    print("NO")
else:
    p = True

    for i in range(2, a):
        if a % i == 0:
            p = False
            break

    if p:
        print("YES")
    else:
        print("NO")