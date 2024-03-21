class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.isFull():
            print("Stack is full")
        else:
            self.top += 1
            self.array[self.top] = item

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.top -= 1
            return self.array[self.top + 1]

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.array[self.top]

    def size(self):
        return self.top + 1


if __name__ == "__main__":
    s = ArrayStack(100)

    msg = input("문자열 입력: ")
    for c in msg:
        s.push(c)

    print("역순 문자열: ", end="")
    while not s.isEmpty():
        print(s.pop(), end="")
    print()
