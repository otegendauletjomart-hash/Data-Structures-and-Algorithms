class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
levelsum = []
def insert(node, value, level):
    if node == None:
        levelsum.append(value)
        return Node(value)
    curr = node
    level = 0

    while True:
        level += 1

        if value < curr.value:
            if curr.left is None:
                curr.left = Node(value)
                if level == len(levelsum):
                    levelsum.append(value)
                else:
                    levelsum[level] += value
                break
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = Node(value)
                if level == len(levelsum):
                    levelsum.append(value)
                else:
                    levelsum[level] += value
                break
            curr = curr.right     
    return node
    

def main():
    j = int(input())
    n = list(map(int, input().split()))

    tree = None

    for i in n:
        tree = insert(tree, i, levelsum)

    print(len(levelsum))
    print(*levelsum)

main()