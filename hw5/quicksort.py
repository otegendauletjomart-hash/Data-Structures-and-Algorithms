
def quick_sort(a):
    if len(a) <= 1:
        return a

    first = a[0]
    middle = a[len(a) // 2]
    last = a[-1]

    pivot = sorted([first, middle, last])[1]

    left = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)


a = [2, 6, 5, 3, 8, 7, 1, 0]

print(quick_sort(a))
