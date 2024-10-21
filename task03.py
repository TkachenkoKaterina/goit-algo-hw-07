class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_sum_of_values(root):
    if root is None:
        return 0
    return (root.val +
            find_sum_of_values(root.left) +
            find_sum_of_values(root.right))


if __name__ == "__main__":
    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    total_sum = find_sum_of_values(root)
    print("Сума всіх значень у дереві:", total_sum)
