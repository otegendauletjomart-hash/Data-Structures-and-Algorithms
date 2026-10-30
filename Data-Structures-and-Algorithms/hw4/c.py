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
        while node is not None:
            if value == node.value:
                return node

            if value < node.value:
                node = node.left
            else:
                node = node.right

        return None

    def subtrees(node):
        stack = [node]

        while stack:
            current = stack.pop()

            if current is None:
                continue

            print(current.value, end=" ")

            stack.append(current.right)
            stack.append(current.left)
            
    j = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = int(input())

    root = bst(a)
    node = search(root, b)

    subtrees(node)
main()
        