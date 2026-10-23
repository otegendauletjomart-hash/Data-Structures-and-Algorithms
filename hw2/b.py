s = int(input())
n = list(map(int, input().split()))

for i in range(len(n)):
    if i%2==0:
        print(n[i], end=" ")