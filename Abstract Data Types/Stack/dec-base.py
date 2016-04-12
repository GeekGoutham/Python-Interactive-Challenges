#Author = Vignesh Goutham
import Stack

def dectobase(number, base):
    out_stack = Stack.Stack()
    out_index = "0123456789ABCDEF"
    out_str = ""
    while number > 0:
        rem = number % base
        out_stack.push(rem)
        number = number // base
    while not out_stack.isEmpty():
        out_str += out_index[out_stack.pop()]
    return out_str

if __name__ == "__main__":
    print(dectobase(25,16))
