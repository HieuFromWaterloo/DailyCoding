"""
1. naive solun O(N):
    - 1st traversion is to count the number of items in a list
    - 2nd traversion is use to traverse up to 1/2 lenght of the list to find the middle node

2. using 2 pointers O(N):
    - 1st pointer goes through the list one by one
    - 2nd pointer goes throught the list 2x as fast (2 element at a time)
    - becuase 2nd pointer is 2x fast, if it reaches the end of the list then it immediately means that the 1st pointer has reached the middle of the list
    - this solution only requires 1 single traversal
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        # while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
        # this while is used to increment the pointers
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node


if __name__ == '__main__':

    linked_list = LinkedList()

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)

    print(linked_list.get_middle_node().data)
