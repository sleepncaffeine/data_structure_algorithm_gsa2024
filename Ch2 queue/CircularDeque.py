from ArrayQueue import ArrayQueue


class CircularDeque(ArrayQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print("Queue is full")

    def deleteRear(self):
        if not self.isEmpty():
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return self.array[self.rear]
        else:
            print("Queue is empty")

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            print("Queue is empty")


dq = CircularDeque()

for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display("odd front, even rear")

for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
dq.display("2 front, 3 rear removed")

for i in range(9, 14):
    dq.addFront(i)
dq.display("9-13 added to front")
