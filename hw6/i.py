s = input()

result = ''

for ch in 'abcdefghijklmnopqrstuvwxyz':
    result += ch * s.count(ch)

print(result)