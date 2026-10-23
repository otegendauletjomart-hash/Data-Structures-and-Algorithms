n = int(input())
s = list(map(int, input().split()))

a = len(s) // 2 
s.pop(a)
print(*s)


