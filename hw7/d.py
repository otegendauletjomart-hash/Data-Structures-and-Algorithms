def merge(a):
    n = len(a)
    result = [0] * n
    left = 0
    right = n-1
    pos = n - 1

    while left <= right:
        if abs(a[left]) > abs(a[right]):
            result[pos] = a[left] ** 2
            left += 1
        else:
            result[pos] = a[right] ** 2
            right -= 1
        pos -= 1

    return result



def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    a = [-4, -1, 0, 3, 10]
    print(merge(a))
main()