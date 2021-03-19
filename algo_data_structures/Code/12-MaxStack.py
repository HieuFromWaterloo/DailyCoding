"""
The aim is to design an algorithm that can return the maximum item of a stack in O(1) running time complexity.
We can use O(N) extra memory

Soln:
Use 2 stacks:
- main stack: keep track of item being inserted into the stack
- max stack: compare each newly pushed item in the main stack with the current max on the max stack
    then keep track of the max then pop at the end with O(1) time
"""

class MaxStack:

    def __init__(self):
        # main stack: use to push
        self.main_stack = []
        self.max_stack = []

    # adding an item to the stack
    # O(1)
    def push(self, data):
        # push new item
        self.main_stack.append(data)

        # the 1st item is the same in both stack
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return None  # if we stop after only inserting 1

        # if item is the largest so far
        # insert to the maxtack
        # return the item withput removing it ==> using peek()
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:  # copy the curent max then push it to the maxstack
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        # pop the current max in the max stack and pop the most recent value in the main stack
        self.max_stack.pop()
        return self.main_stack.pop()

    def get_max(self):
        # max is the most recent item inserted in the max stack at O(1)
        return self.max_stack.pop()


if __name__ == '__main__':
    max_stack = MaxStack()
    max_stack.push(1000)
    max_stack.push(1)
    max_stack.push(5)
    max_stack.push(2)
    max_stack.push(20)
    print(max_stack.get_max())
