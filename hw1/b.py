a, b, m = map(int, input().split())

r = 1
while b != 0:
    if b % 2 == 0:
        a = (a * a) % m
        b = b//2
        
    else: 
        b = b - 1
        r = (a * r) % m

print(r%m)