from classStack import ArrayStack


def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ("{[("):
            stack.push(ch)
        elif ch in ("}])"):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (
                    (ch == "}" and left != "{")
                    or (ch == "]" and left != "[")
                    or (ch == ")" and left != "(")
                ):
                    return False
    return stack.isEmpty()


if __name__ == "__main__":
    expressions = [
        "{A[(i+1)]} = 7",
        "3*(A[i]+5)",
        "3*(A[i]+5",
        "{(A+B)-3}*5+[{cos(x+y)+7]-1}*9",
    ]
    for expr in expressions:
        res = checkBrackets(expr)
        print(expr, "--->", res)
