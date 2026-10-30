def quick_sort(a):
    if len(a) <= 1:
        return a

    last = a[-1]
    middle = a[len(a)//2]
    first = a[0]

    pivot = sorted([first, middle, last])[1]

    left = [x for x in a if x < pivot]
    eq = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return quick_sort(left) + eq + quick_sort(right)


a = [6, 5, 3, 9]
ans = 0

while len(a) > 1:
    q = quick_sort(a)

    x = q.pop(0)
    y = q.pop(0)

    s = x + y
    ans += s

    q.append(s)
    a = q

print(ans)
