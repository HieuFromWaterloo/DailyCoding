# LIFO

class Stack:
    # we use array to implement stack
    def __init__(self):
        self.stack = []

    # O(1)
    def size_stack(self):
        return len(self.stack)

    # O(1) running time
    def push(self, data):
        # insert
        self.stack.append(data)

    # O(1) because we manipulate the last item
    def pop(self):
        # if stack is empty
        if self.size_stack() < 1:  # if is_empty(self):
            return None

        data = self.stack[-1]
        # self.stack.remove(data)
        del self.stack[-1]
        return data

    # O(1) constant running time
    def peek(self):
        return self.stack[-1]

     # O(1) running time
    def is_empty(self):
        return self.stack == []


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    # print(f"Stack: {print(stack)}")
    print(f"Size: {stack.size_stack()}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
