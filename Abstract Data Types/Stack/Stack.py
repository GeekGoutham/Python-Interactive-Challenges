#Author = Vignesh Goutham

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)              #O(1)

    def pop(self):
        return self.stack.pop()                 #O(1)

    def peek(self):
        return self.stack[len(self.stack)-1]    #O(n)

    def isEmpty(self):
        return (len(self.stack) == 0)           #O(n)

    def printStack(self):                       #O(n)
        print(self.stack)


