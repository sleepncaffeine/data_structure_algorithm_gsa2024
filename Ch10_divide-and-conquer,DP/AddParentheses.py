def diffWaysToCompute(expr):
    left = 0
    right = 0
    res = []
    for i in range(len(expr)):
        if expr[i] in "+-*":
            left = diffWaysToCompute(expr[:i])
            right = diffWaysToCompute(expr[i + 1 :])
            for l in left:
                for r in right:
                    if expr[i] == "+":
                        res.append(l + r)
                    elif expr[i] == "-":
                        res.append(l - r)
                    else:
                        res.append(l * r)

    if not res:
        res.append(int(expr))
    return res


print(diffWaysToCompute("2*3-4*5"))
print(diffWaysToCompute("2-1-1"))


class Diff:
    def diff(self, input):
        def calc(left, right, op):
            res = []
            for l in left:
                for r in right:
                    res.append(eval(str(l) + op + str(r)))
            return res

        if input.isdigit():
            return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diff(input[:i])
                right = self.diff(input[i + 1 :])
                res.extend(calc(left, right, input[i]))
        return res
