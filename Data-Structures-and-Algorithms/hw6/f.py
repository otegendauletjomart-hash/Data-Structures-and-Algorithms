grade_scale = {
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "C+": 2.50,
    "C": 2.00,
    "D+": 1.50,
    "D": 1.00,
    "F": 0.00,
}
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
            if left[i][2] < right[j][2]:
                a[k] = left[i]
                i += 1
            elif left[i][2] > right[j][2]:
                a[k] = right[j]
                j += 1
            elif left[i][0] < right[j][0]:
                a[k] = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                a[k] = right[j]
                j += 1
            elif left[i][1] < right[j][1]:
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
        
def GPA(a,m):
    total_points = 0.0
    total_credits = 0

    for i in range(0, m*2, 2):
        grade = a[i]
        credits = int(a[i+1])

        total_points += grade_scale[grade] * credits
        total_credits += credits

    return total_points/total_credits  


def main():
    n = int(input())
    mas = []
    for i in range(n):
        data = list(input().split())
        surname = data[0]
        name = data[1]
        m = int(data[2])
        a = data[3:]
        gpa = GPA(a, m)
        mas.append([surname, name, gpa])
    
    merge_sort(mas)
    for i in mas:
        print(i[0], i[1], f"{i[2]:.3f}")

main()