def mergeit(a):
    if len(a) > 1:
        left = a[:len(a)//2]
        right = a[len(a)//2:]

        mergeit(left)
        mergeit(right)

        i = 0
        j = 0
        k = 0
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while len(left) > i:
            a[k] = left[i]
            i += 1
            k += 1
        while len(right) > j:
            a[k] = right[j]
            j += 1
            k += 1

def main():
    n = int(input())
    data = []
    for i in range(n):
        d = list(input().split())
        mergeit(d)
        data.append(d)

    print(*data)

main()