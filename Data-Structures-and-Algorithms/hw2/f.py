n = list(map(int, input().split()))
m = list(map(int, input().split()))

a = n[1:]
b = m[1:]

r = []

i = 0
j = 0

while i < len(a) and j < len(b):

    if a[i] > b[j]:
        r.append(b[j])
        j += 1
    else:
        r.append(a[i])
        i += 1

while i < len(a):
    r.append(a[i])
    i += 1

while j < len(b):
    r.append(b[j])
    j += 1

print(*r)