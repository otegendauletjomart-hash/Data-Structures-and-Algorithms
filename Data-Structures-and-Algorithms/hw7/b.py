def merge(a):
    if len(a) > 1:
        left = a[:len(a)//2]
        right = a[len(a)//2:]

        merge(left)
        merge(right)

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
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    data = []
    data.extend(a)
    data.extend(b)
    merge(data)
    print(*data)

         

main()