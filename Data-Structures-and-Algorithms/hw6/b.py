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

        while len(left) > i:
           a[k] =  left[i]
           i += 1
           k += 1
        while len(right) > j:
            a[k] = right[j]
            j += 1
            k += 1
        


n, m = map(int, input().split())

a = list(map(int, input().split())) if n > 0 else []
b = list(map(int, input().split())) if m > 0 else []
merge_sort(a)
merge_sort(b)
i = 0
j = 0
ans = []

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        ans.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1 
    elif a[i] > b[j]:
        j += 1

print(*ans)