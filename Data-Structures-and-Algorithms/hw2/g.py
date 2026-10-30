class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
tail = None

n = list(map(int, input().split()))
words = input().split()
k = n[1]
for i in words:
    new_node = Node(i)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

if k == 0 or k == n:
    current = head

else:
    current = head

    for i in range(k - 1):
        current = current.next

    new_head = current.next

    current.next = None

    current = new_head

    while current.next is not None:
        current = current.next

    current.next = head

    head = new_head

current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next