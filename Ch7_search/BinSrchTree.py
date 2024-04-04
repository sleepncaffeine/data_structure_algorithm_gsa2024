class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"({self.key}, {self.value})"


def search_bst(n, key):
    if n == None:
        return None
    if key == n.key:
        return n
    if key < n.key:
        return search_bst(n.left, key)
    return search_bst(n.right, key)


def search_value_bst(n, value):
    if n == None:
        return None
    if value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res != None:
        return res
    return search_value_bst(n.right, value)


def insert_bst(root, node):
    if root == None:
        return node
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    return root


def delete_bst(root, key):
    if root == None:
        return root

    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)

    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left

        succ = root.right
        while succ.left != None:
            succ = succ.left
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)

    return root


def print_node(msg, n):
    print(msg, n if n != None else "Search Failed")


def preorder(r):
    if r != None:
        print(r.key, end=" ")
        preorder(r.left)
        preorder(r.right)


def print_tree(msg, r):
    print(msg, end=" ")
    preorder(r)
    print()


data = [
    (6, "Six"),
    (8, "Eight"),
    (3, "Three"),
    (5, "Five"),
    (9, "Nine"),
    (7, "Seven"),
    (2, "Two"),
    (4, "Four"),
]

root = None
for i in range(0, len(data)):
    root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

print_tree("Initial:", root)

n = search_bst(root, 5)
print_node("Search 5:", n)
