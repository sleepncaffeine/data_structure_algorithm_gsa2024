capacity = 10
array = [None] * capacity
top = -1


def isEmpty():
    if top == -1:
        return True
    else:
        return False


def isFull():
    return top == capacity - 1


def push(data):
    global top
    if isFull():
        print("Stack is full")
    else:
        top += 1
        array[top] = data


def peek():
    if isEmpty():
        print("Stack is empty")
    else:
        return array[top]


def size():
    return top + 1


def pop():
    global top
    if isEmpty():
        print("Stack is empty")
    else:
        data = array[top]
        array[top] = None
        top -= 1
        return data


if __name__ == "__main__":
    msg = input("문자열 입력: ")
    for c in msg:
        push(c)

    print("문자열 출력: ", end="")

    while not isEmpty():
        print(pop(), end="")

    print()
