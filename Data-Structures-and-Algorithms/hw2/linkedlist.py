class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
tail = None

words = input().split()

for i in words:
    new_node = Node(i)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next

