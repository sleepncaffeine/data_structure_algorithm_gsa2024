from ArrayQueue import ArrayQueue
import random

q = ArrayQueue(8)

q.display("Initial queue")

while not q.isFull():
    q.enqueue(random.randint(0, 100))
q.display("Full queue")

print("Dequeing order: ", end="")
while not q.isEmpty():
    print(q.dequeue(), end=" ")
print("\n")
