def get_jj(l):
    d = []
    for i in l:
        if i == "#":
            if d:
                d.pop()
        else:
            d.append(i)
    return "".join(d)

a = input()
b = input()

a = get_jj(a)
b = get_jj(b)

if a == b:
    print("Yes")
else: 
    print("No")