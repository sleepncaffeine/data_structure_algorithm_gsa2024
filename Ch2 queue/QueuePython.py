import queue
import random

q = queue.Queue(8)

print("Inserting order: ", end="")
while not q.full():
    v = random.randint(0, 100)
    q.put(v)
    print(v, end=" ")
print()

print("Dequeing order: ", end="")
while not q.empty():
    print(q.get(), end=" ")
print()

########################

import collections

dq = collections.deque()

print("Deque is not empty" if dq else "Deque is empty")
for i in range(9):
    if i % 2 == 0:
        dq.append(i)
    else:
        dq.appendleft(i)
print("odd front, even rear =", dq)

for i in range(2):
    dq.popleft()
for i in range(3):
    dq.pop()
print("2 front, 3 rear removed =", dq)

for i in range(9, 14):
    dq.appendleft(i)

print("9-13 added to front =", dq)

print("Deque is not empty" if dq else "Deque is empty")
