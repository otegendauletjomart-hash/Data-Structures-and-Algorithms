def prefix_func(t):
    p = [0] * len(t)
    j = 0
    i = 1

    while i < len(t):
        if t[j] == t[i]:
            j += 1
            p[i] = j
            i += 1
        elif j > 0:
            j = p[j - 1]
        else:
            p[i] = 0
            i += 1

    return p


def kmp(g, a):
    p = prefix_func(g)
    i = 0
    j = 0

    while i < len(a):
        if a[i] == g[j]:
            i += 1
            j += 1

            if j == len(g):
                return True
        elif j > 0:
            j = p[j - 1]
        else:
            i += 1

    return False


a = "abcd"
b = "cdabcdab"

k = (len(b) + len(a) - 1) // len(a)

if kmp(b, a):
    print(1)
elif kmp(b, a * k):
    print(k)
elif kmp(b, a * (k + 1)):
    print(k + 1)
else:
    print(-1)