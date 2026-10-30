boris = list(map(int, input().split()))
nursik = list(map(int, input().split()))
c = 0
while len(boris) != 0 and len(nursik) != 0:
    b = boris.pop(0)
    n = nursik.pop(0)
    if b == 0 and n == 9:
        boris.append(b)
        boris.append(n)
    elif n == 0 and b == 9:
        nursik.append(n)
        nursik.append(b)
    else:
        if b > n:
            boris.append(b)
            boris.append(n)
        else:
            nursik.append(n)
            nursik.append(b)
    c += 1

if len(boris) == 0:
    print("Nursik " + str(c))
else:
    print("Boris " + str(c))