s = input()
stack = []

for char in s:
    if stack and stack[-1] == char:
        stack.pop()  
    else:
        stack.append(char)  

if len(stack) == 0:
    print("YES")
else:
    print("NO")