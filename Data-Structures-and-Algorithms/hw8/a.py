MOD = 10**9 + 7

def hash_string(s):
    h = 0

    for i in range(len(s)):
        h += (ord(s[i]) - 47) * (11 ** i)

    return h % MOD


n = int(input())

data = []

for i in range(2 * n):
    data.append(input().strip())

data_set = set(data)
pairs = {}

for s in data:
    h = str(hash_string(s))

    if h in data_set and h != s:
        pairs[s] = h

for s in data:
    if s in pairs:
        print(f'Hash of string "{s}" is {pairs[s]}')