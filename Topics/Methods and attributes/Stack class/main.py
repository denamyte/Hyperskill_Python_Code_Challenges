class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return None if self.is_empty() else self.stack.pop()

    def peek(self):
        return None if self.is_empty() else self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def test():
    s = Stack()
    for v in range(5):
        s.push(v)
    print(s.stack)
    print(s.pop())
    print(s.stack)
    print(s.peek())
    print(s.peek())
    print(s.stack)
    for _ in range(6):
        print(s.pop())
    print(s.stack)


# test()