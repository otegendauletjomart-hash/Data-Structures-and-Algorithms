import re

def merge_sort(a):
    if len(a) > 1:
        left_arr = a[:len(a)//2]
        right_arr = a[len(a)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0 
        k = 0 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                a[k] = left_arr[i]
                i += 1
            else:
                a[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            a[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            a[k] = right_arr[j]
            j += 1
            k += 1


s = "hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozv"
glass = re.findall(r"[aeiou]", s)
neglass = re.findall(r"[^aeiou]", s)

merge_sort(glass)
merge_sort(neglass)

print(''.join(glass + neglass))
