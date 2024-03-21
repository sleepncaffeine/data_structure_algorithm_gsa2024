from BinaryTree import *


def evaluate(node):
    if node is None:
        return 0
    elif node.isLeaf():
        return node.data
    else:
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == "+":
            return op1 + op2
        elif node.data == "-":
            return op1 - op2
        elif node.data == "*":
            return op1 * op2
        elif node.data == "/":
            return op1 / op2


def buildTree(expr):
    if not len(expr):
        return None

    token = expr.pop(0)
    if token in "+-*/":
        node = BTNode(token)
        node.right = buildTree(expr)
        node.left = buildTree(expr)
        return node
    else:
        return BTNode(float(token))


str = input("Enter an expression(postfix): ")
expr = str.split()
print("tokens: ", expr)
root = buildTree(expr)
print("\nPreorder:", end=" ")
preorder(root)
print("\nInorder:", end=" ")
inorder(root)
print("\nPostorder:", end=" ")
postorder(root)
print("\nResult: ", evaluate(root))
