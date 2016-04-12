#Author = Vignesh Goutham
import Stack

def eval_parantheses(StringSymbol):
    mismatch = False
    for sym in StringSymbol:
        if sym == "(":
            s.push(sym)
        elif sym == ")" and s.isEmpty() == False:
            s.pop()
        else:
            mismatch = True
    if (s.isEmpty() == False):
        mismatch = True

    return (not mismatch)




if __name__ == "__main__":
    s = Stack.Stack()
    res = eval_parantheses("((")
    print(res)