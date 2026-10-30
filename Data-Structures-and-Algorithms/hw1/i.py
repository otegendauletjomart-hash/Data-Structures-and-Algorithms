t = int(input())

for i in range(t):
    n = int(input())

    deck = []

    for k in range(n, 0, -1):

        deck.insert(0, k)

        m = len(deck)
        x = k % m

        deck = deck[-x:] + deck[:-x] if x != 0 else deck

    print(*deck)