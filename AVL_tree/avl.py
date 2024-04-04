class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n is None:
            return 0
        return n.height

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value, 1)
        if key < n.key:
            n.left = self.put_item(n.left, key, value)
        elif key > n.key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            return self.rotate_right(n)
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            return self.rotate_left(n)
        return n

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def delete(self, key):
        self.root = self.delete_item(self.root, key)

    def delete_item(self, n, key):
        if n is None:
            return None
        if key < n.key:
            n.left = self.delete_item(n.left, key)
        elif key > n.key:
            n.right = self.delete_item(n.right, key)
        else:
            if n.right is None:
                return n.left
            if n.left is None:
                return n.right
            target = n
            n = self.min(target.right)
            n.right = self.delete_min(target.right)
            n.left = target.left
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def delete_min(self, n):
        if n.left is None:
            return n.right
        n.left = self.delete_min(n.left)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def min(self, n):
        if n is None:
            return None
        return self.min_item(n)

    def min_item(self, n):
        if n.left is None:
            return n
        return self.min_item(n.left)

    def preorder(self, n):
        if n is not None:
            print(str(n.key) + " ", end="")
            self.preorder(n.left)
            self.preorder(n.right)

    def inorder(self, n):
        if n is not None:
            self.inorder(n.left)
            print(str(n.key) + " ", end="")
            self.inorder(n.right)
