
def prefix(t):
    p = [0] * len(t)
    i = 1
    j = 0

    while i < len(t):
        if t[j] == t[i]:
            j += 1
            p[i] = j
            i += 1
        elif j > 0:
            j = p[j-1]
        else:
            p[i] = 0
            i += 1

    return p

a = "asas"
k = 4
n = len(a)
p = prefix(a)
answer = n + (k - 1) * (n - p[-1])
