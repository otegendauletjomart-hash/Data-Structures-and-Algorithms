def merge_sort(a):
    if len(a) > 1:
        left = a[:len(a)//2]
        right = a[len(a)//2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1


n = int(input())
dates = []

for _ in range(n):
    day, month, year = map(int, input().split("-"))
    dates.append((year, month, day))

merge_sort(dates)

for year, month, day in dates:
    print(f"{day:02d}-{month:02d}-{year:04d}")