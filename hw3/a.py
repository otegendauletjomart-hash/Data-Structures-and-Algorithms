def binary_search(seq, item):
    begin_index = 0
    end_index = len(seq) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = seq[midpoint]
        if midpoint_value == item:
            return "YES"
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return "NO"



n = int(input())
a = list(map(int, input().split()))
f = int(input())



print(binary_search(a, f))

