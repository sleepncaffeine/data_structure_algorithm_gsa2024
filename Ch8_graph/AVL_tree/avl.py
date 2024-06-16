class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

    # 노드 생성자
    # key, value, 노드 높이, 좌/우 자식 레퍼런스


class AVL:
    def __init__(self):
        self.root = None  # 트리 루트

    def height(self, n):
        if n is None:
            return 0
        return n.height  # 노드 n의 높이 반환

    def put(self, key, value):  # 삽입 연산
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value, 1)  # 높이 1인 새 노드 생성
        if key < n.key:
            n.left = self.put_item(n.left, key, value)
        elif key > n.key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value  # key 이미 있으면 value만 갱신
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        # ↑ n의 높이 갱신
        return self.balance(n)  # n의 불균형 처리

    def balance(self, n):  # 불균형 처리
        # 노드 n에서 불균형 발생
        if self.bf(n) > 1:  # 왼쪽 자식이 높음
            if self.bf(n.left) < 0:  # 왼쪽 자식의 우측 서브트리가 높음
                n.left = self.rotate_left(n.left)  # LR 회전
            n = self.rotate_right(n)  # LL 회전

        elif self.bf(n) < -1:  # 오른쪽 자식이 높음
            if self.bf(n.right) > 0:  # 오른쪽 자식의 왼쪽 서브트리가 높음
                n.right = self.rotate_right(n.right)  # RL 회전
            n = self.rotate_left(n)  # RR 회전
        return n

    def bf(self, n):  # bf 계산
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):  # 우로 회전
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n):  # 좌로 회전
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def delete(self, key):  # 삭제 연산
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

    def delete_min(self, n):  # 최솟값 삭제
        if n.left is None:
            return n.right
        n.left = self.delete_min(n.left)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def min(self, n):  # 최솟값 찾기
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
