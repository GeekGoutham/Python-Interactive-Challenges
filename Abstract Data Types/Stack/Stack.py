#Author = Vignesh Goutham

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return (len(self.stack) == 0)

    def printStack(self):
        print(self.stack)

if __name__ == "__main__":
    s = Stack()
    s.push("VG")
    s.push("Goutham")
    print(s.pop())
