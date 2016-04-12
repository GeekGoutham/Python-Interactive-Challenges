#Author = Vignesh Goutham

import Stack

def dectobin(decnumber):
    bin_stack = Stack.Stack()

    while (decnumber > 0):
        rem = decnumber % 2
        bin_stack.push(rem)
        decnumber = decnumber // 2
    bin_num_str = ""
    while not bin_stack.isEmpty():
        bin_num_str += str(bin_stack.pop())
    return int(bin_num_str)


if __name__ == "__main__":
    print(dectobin(233))
