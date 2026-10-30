class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(data):
    head = None
    tail = None

    for value in data:
        new_node = Node(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


def merge(a, b):
    if a is None:
        return b

    if b is None:
        return a

    if a.value <= b.value:
        head = a
        a = a.next
    else:
        head = b
        b = b.next

    tail = head

    while a is not None and b is not None:

        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next

        tail = tail.next

    if a is not None:
        tail.next = a
    else:
        tail.next = b

    return head


def print_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next


data = list(map(int, input().split()))
n = data[0]
a = data[1:]

data = list(map(int, input().split()))
m = data[0]
b = data[1:]

head_a = build_list(a)
head_b = build_list(b)

head = merge(head_a, head_b)

print_list(head)