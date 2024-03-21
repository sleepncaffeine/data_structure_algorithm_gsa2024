class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.next = next
        self.prev = prev

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node

    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if node.next is not None:
                node.next.prev = self
        return node


class DblLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def isFull(self):
        return False

    def getNode(self, pos):
        if pos < 0:
            return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def display(self, msg="DblLinkedList: "):
        print(msg, end="")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end="<=>")
            ptr = ptr.next
        print("None")

    def size(self):
        ptr = self.head
        cnt = 0
        while ptr is not None:
            ptr = ptr.next
            cnt += 1
        return cnt

    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos - 1)
        if before == None:
            node.next = self.head
            if self.head is not None:
                self.head.prev = node
            self.head = node
        else:
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            before = self.head
            if before is not None:
                self.head = before.next
            if self.head is not None:
                self.head.prev = None
            return before
        else:
            before.popNext()

    def replace(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos - 1)
        if before == None:
            node.next = self.head.next
            node.prev = self.head.prev
            self.head = node
        else:
            node.append(before.popNext())
            before.append(node)


s = DblLinkedList()
s.display("LinkedList(initial): ")
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("LinkedList(insert x5): ")
s.replace(2, 90)
s.display("LinkedList(replace x1): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("LinkedList(delete x3): ")
