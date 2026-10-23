def compare(row1, row2):
    sum1 = sum(row1)
    sum2 = sum(row2)

    if sum1 !=  sum2:
        return sum1 > sum2

    return row1 < row2


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
            if compare(left[i], right[j]):
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
    #n, m = map(int, input().split())
    #data = []

    #for i in range(n):
    #    a = list(map(int, input().split()))
    #    data.append(a)
    data = [[1, 2, 3], [1, 2, 4], [1, 3, 2], [6, 0, 0], [2, 3, 2]]
    merge(data)
    for row in data:
        print(*(row))

main()