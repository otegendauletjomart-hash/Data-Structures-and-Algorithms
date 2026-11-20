def hash(s):
    h = 0

    for i in range(len(s)):
        h += (ord(s[i])-47) * (11 ** i)

    return h % (10**9 + 7)

def main():
    n = int(input())
    data = []

    for i in range(2*n):
        data.append(input().strip())

    sett = set(data)
    pair = {}
    order = []

    for s in data:
        h = str(hash(s))

        if h in sett and h != s:
            pair[s] = h
            order.append(s)

    for s in order:
        print(f'Hash of string "{s}" is {pair[s]}') 
        

main()