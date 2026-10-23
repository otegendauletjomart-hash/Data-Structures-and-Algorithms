n = int(input())
names = []
for j in range(n):
   name = input()
   names.append(name)

d = [names[0]]

for i in range(1, len(names)):
    if names[i-1] != names[i]:
        d.append(names[i])

print(len(d))
print(*d, sep="\n")