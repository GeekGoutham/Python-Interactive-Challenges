#Author = Vignesh Goutham
import Stack

def eval_parantheses(StringSymbol):
    mismatch = False
    for sym in StringSymbol:
        if sym in "({[":
            s.push(sym)
        elif sym in ")}]" and s.isEmpty() == False:
            top = s.pop()
            match_res = matches(sym,top)
            if not match_res:
                mismatch = True
        else:
            mismatch = True
    if (s.isEmpty() == False):
        mismatch = True

    return (not mismatch)


def matches(sym,top):
    opens = "({["
    closers = ")}]"
    return opens.index(top) == closers.index(sym)

if __name__ == "__main__":
    s = Stack.Stack()
    res = eval_parantheses("(({}))")
    print(res)