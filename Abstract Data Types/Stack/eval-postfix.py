#Author = Vignesh Goutham
import Stack

def evaluate_postfix(expr):
    s = Stack.Stack()
    for ex in expr:
        if ex in "0123456789":
            s.push(ex)
        elif ex in "*/+-":
            b = int(s.pop())
            a = int(s.pop())
            res = evalMath(a,b,ex)
            s.push(res)
    return s.pop()


def evalMath(a,b,ex):
    if ex == "*":
        res = a * b
    elif ex == "/":
        res = a / b
    elif ex == "+":
        res = a + b
    elif ex == "-":
        res = a - b
    return res


if __name__ == "__main__":
    print(evaluate_postfix("3232*+"))