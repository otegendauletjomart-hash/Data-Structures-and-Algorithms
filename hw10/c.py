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
    c = 0

    while i < len(a):
        if a[i] == g[j]:
            i += 1
            j += 1

            if j == len(g):
                return i-j

        elif j > 0:
            j = p[j - 1]
        else:
            i += 1

    return -1


a = "zabcd"
b = "abcdz"

bb = b*2
print(kmp(a, bb))

