#Author = Vignesh Goutham
import Stack

def evaluate_postfix(expr_raw):             #Postfix expressions always have spaces since that is the way two digits can be identified
    expr = expr_raw.split(" ")
    s = Stack.Stack()
    for ex in expr:
        if ex.isdigit():
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
    print(evaluate_postfix("3 20 2 * +"))