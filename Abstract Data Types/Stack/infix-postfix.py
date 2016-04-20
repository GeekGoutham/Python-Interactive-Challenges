#Author = Vignesh Goutham
import Stack

def infixtopostfix(expr_raw):               #Can add implmentaton to check if the braces are balanced
    expr_stack = Stack.Stack()
    expr = expr_raw.split(" ")
    str_out = ""
    prec = {"*":3,"/":3,"+":2,"-":2,"(":1,")":1}
    out_list = list()
    for ch in expr:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or ch.isdigit():
            out_list.append(ch)
        elif ch == "(":
            expr_stack.push(ch)
        elif ch == ")":
            pop_token = expr_stack.pop()
            while pop_token != "(":
                out_list.append(pop_token)
                pop_token = expr_stack.pop()
        else:
            while (not expr_stack.isEmpty()) and (prec[ch] <= prec[expr_stack.peek()]):
                popped = expr_stack.pop()
                out_list.append(popped)
            expr_stack.push(ch)
    while (not expr_stack.isEmpty()):
        out_list.append(expr_stack.pop())
    for chi in out_list:
        str_out += " " + str(chi)
    return str_out

if __name__ == "__main__":
    print(infixtopostfix("10 + 3 * 5 / ( 16 - 4 )"))
    #A + B * C