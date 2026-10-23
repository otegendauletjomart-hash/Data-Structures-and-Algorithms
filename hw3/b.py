def binary_search(seq, item):
    begin_index = 0
    end_index = len(seq) - 1
    answer = len(seq)

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = seq[midpoint]

        if midpoint_value >= item:
            answer = midpoint
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1

    return answer
    
a = [21, 1, 2, 3, 5, 8, 13]
q1 = [1, 5, 13, 21]
q2 = [1, 1, 2, 3]
q3 = [1, 3, 2, 8]

a.sort()

l1 = q1[0]
l2 = q1[1]
r1 = q1[2]
r2 = q1[3]

g = binary_search(a, 5)


print(g)

