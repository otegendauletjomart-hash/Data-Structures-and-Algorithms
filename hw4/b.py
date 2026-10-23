class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def main():
    def insert(node, value):
        new_node = Node(value)

        if node is None:
            return new_node

        current = node

        while True:
            if value < current.value:
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
    def bst(value):
        root = None

        for i in value:
            root = insert(root, i)

        return root

    def search(node, value):
        if node is None:
            return None

        if value == node.value:
            return node

        if value < node.value:
            return search(node.left, value)
        else:
            return search(node.right, value)

    def size(node):
        if node is None:
            return 0

        stack = [node]
        count = 0

        while stack:
            current = stack.pop()
            count += 1

            if current.left is not None:
                stack.append(current.left)

            if current.right is not None:
                stack.append(current.right)

        return count
        
            
    j = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = int(input())

    root = bst(a)
    node = search(root, b)

    print(size(node))
main()
        