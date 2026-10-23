n = int(input())

orig = {}
cur = {}

for i in range(n):
    old, new = input().split()
    
    if old in orig:
        o = orig.pop(old)
    else:
        o = old
        
    orig[new] = o
    cur[o] = new

print(len(cur))
for o in sorted(cur):
    print(o, cur[o])