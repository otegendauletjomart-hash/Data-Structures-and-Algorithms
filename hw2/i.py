class Node:
    def init(self, data):
        self.data = data
        self.next = None
        self.prev = None

head = None
tail = None

while True:
    command = input().split()

    if command[0] == "add_front":
        node = Node(command[1])

        if head is None:
            head = node
            tail = node
        else:
            node.next = head
            head.prev = node
            head = node
        print("ok")
    
    elif command[0] == "add_back":
        node = Node(command[1])

        if tail is None:
            head = node
            tail = node
        else:
            node.prev = tail
            tail.next = node
            tail = node
        print("ok")
    
    elif command[0] == "erase_front":
        if head is None:
            print("error")
        else:
            print(head.data)

            if head == tail:
                head = None
                tail = None
            else:
                head = head.next
                head.prev = None
    
    elif command[0] == "erase_back":
        if tail is None:
            print("error")
        else:
            print(tail.data)

            if head == tail:
                head = None
                tail = None
            else:
                tail = tail.prev
                tail.next = None

    elif command[0] == "front":
        if head is None:
            print("error")
        else:
            print(head.data)

    elif command[0] == "back":
        if tail is None:
            print("error")
        else:
            print(tail.data)
    
    elif command[0] == "clear":
        head = None
        tail = None
        print("ok")
    
    elif command[0] == "exit":
        print("goodbye")
        break