def main():   
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

    def insert(node, value):
        new_node = Node(value)

        if node is None:
            return new_node

        current = node     

        while True:
            if value <= current.value:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

        return node        

    def bst(values):
        root = None

        for value in values:
            root = insert(root, value)

        return root

    def find(node, road):
        for direction in road:
            if node is None:
                return "NO"
            if direction == "L":
                node = node.left

            else:
                node = node.right

        if node is None:
            return "NO"
        
        return "YES"

    j = list(map(int, input().split()))
    a = list(map(int, input().split()))
    root = bst(a)
    anwser = []
    for i in range(j[1]):
        b = input().strip()
        anwser.append(find(root, b))


    for l in anwser:
        print(l)        

main()