from ArrayQueue import ArrayQueue


class RingBuffer(ArrayQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def enqueue(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity


q = RingBuffer(8)

q.display("Initial queue")
for i in range(6):
    q.enqueue(i)
q.display("0-5 inserted")

q.enqueue(6)
q.enqueue(7)
q.display("6-7 inserted")

q.enqueue(8)
q.enqueue(9)
q.display("8-9 inserted")

q.dequeue()
q.dequeue()
q.display("Two items removed")
