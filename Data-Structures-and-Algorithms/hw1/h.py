n = int(input())
a = list(map(int, input().split()))

stack = []
ans = []

for age in a:
    while stack and stack[-1] >= age:
        stack.pop()

    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)

    stack.append(age)

print(*ans)