def get_prime(p):
    d = []

    for i in range(2, p):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            d.append(i)
    return d
def get_simple_prime(a):
    p1 = get_prime(a)
    f = []

    while a != 1:
        for i in p1:
            if a % i == 0:
                f.append(i)
                a = a // i
                break
    return f


a = int(input())
b = int(input())

i = get_simple_prime(a)
j = get_simple_prime(b)

similar = True
eyob = []
d = 0
s = 0
for num in i:
    if num in j:
        eyob.append(num)
        j.remove(num)

fin = 1

for i in eyob:
    fin = fin * i

print(fin)