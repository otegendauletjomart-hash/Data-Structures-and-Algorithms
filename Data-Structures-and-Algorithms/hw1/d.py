a = int(input())

c = 0
n = 2

while c < a:
    p = True

    for i in range(2, n):
        if n % i == 0:
            p = False
            break

    if p:
        c += 1

    n += 1

print(n - 1)