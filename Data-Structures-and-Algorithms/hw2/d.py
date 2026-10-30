n = int(input())
playlist = list(map(int, input().split()))
for i in range(len(playlist)-1, -1, -1):
    print(playlist[i], end=" ")
    