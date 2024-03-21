class BTNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None


def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)


def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)


def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")


import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Ch2_queue import ArrayQueue


def levelorder(n):
    q = ArrayQueue.ArrayQueue()
    q.enqueue(n)
    while not q.isEmpty():
        n = q.dequeue()
        if n is not None:
            print(n.data, end=" ")
            q.enqueue(n.left)
            q.enqueue(n.right)


def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)


def calc_height(n):
    if n is None:
        return 0
    else:
        hLeft = calc_height(n.left)
        hRight = calc_height(n.right)

        if hLeft > hRight:
            return 1 + hLeft
        else:
            return 1 + hRight


if __name__ == "__main__":
    d = BTNode("D")
    e = BTNode("E")
    b = BTNode("B", d, e)
    f = BTNode("F")
    c = BTNode("C", f)
    root = BTNode("A", b, c)

    print("\nInorder: ", end="")
    inorder(root)
    print("\nPreorder: ", end="")
    preorder(root)
    print("\nPostorder: ", end="")
    postorder(root)
    print("\nLevelorder: ", end="")
    levelorder(root)
    print()

    print("Number of nodes:", count_node(root))
    print("Height of tree:", calc_height(root))
