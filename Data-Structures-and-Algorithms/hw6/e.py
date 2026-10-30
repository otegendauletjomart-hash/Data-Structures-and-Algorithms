def merge_sort(a):
    if len(a) > 1:
        left = a[:len(a)//2]
        right = a[len(a)//2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i<len(left) and j<len(right):
            if left[i] > right[j]:
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

def main():
    n,m = map(int, input().split())

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    for c in range(m):
        column = []

        for i in range(n):
            column.append(a[i][c])

        merge_sort(column)

        for i in range(n):
            a[i][c] = column[i]

    for i in range(n):
        print(*a[i])

main()