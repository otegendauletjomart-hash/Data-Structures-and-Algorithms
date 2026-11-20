
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


def main():
    a = input().lower()
    n = int(input())

    res = []

    for _ in range(n):
        city = input().strip()
        b = city.lower() + "#" + a
        p = prefix(b)

        length = p[-1]
        res.append((city, length))

    maxlen = max(length for city, length in res)

    ans = []
    for city, length in res:
        if length == maxlen:
            ans.append(city)

    print(len(ans))
    for city in ans:
        print(city)


main()


