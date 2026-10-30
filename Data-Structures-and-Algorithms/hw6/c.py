n = int(input())
a = sorted(map(int, input().split()))

d = min(a[i + 1] - a[i] for i in range(n - 1))

result = []
for i in range(n - 1):
    if a[i + 1] - a[i] == d:
        result.append(a[i])
        result.append(a[i + 1])

print(*result)