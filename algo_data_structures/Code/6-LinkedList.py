class Node:

    def __init__(self, data):
        # data
        self.data = data
        # reference
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # O(1)
    def insert_start(self, data):
        # Instantiation: increment number of nodes
        self.num_of_nodes = self.num_of_nodes + 1
        new_node = Node(data)

        # the head is NULL (so the data structure is empty)
        # if linklist does not exist with a head node
        if not self.head:
            self.head = new_node
        # there is at laest one item in the linked list
        else:
            # new item inserted will be the new head node poiting to the previous node
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        # Instantiation: increment number of nodes
        self.num_of_nodes = self.num_of_nodes + 1
        new_node = Node(data)

        # the actual_node points to the current head node
        actual_node = self.head

        # we have to find the end of the linked list in O(N) linear running time
        # while actual_node not pointing to NULL, which is the last node
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        # actual_node is the last node: so we insert the new_node right after the actual_node
        actual_node.next_node = new_node

    # O(1)
    def size_of_list(self):
        return self.num_of_nodes

    # have to consider all the items in O(N) linear running time
    def traverse(self):
        # instantiate the head node
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    # O(N) linear running time for finding arbitrary item
    def remove(self, data):

        # list is empty
        if self.head is None:
            return None

        # start with the head
        actual_node = self.head
        # we have to track the previous node for future pointer updates
        # this is why doubly linked lists are better - we can get the previous
        # node (here with linked lists it is impossible)
        previous_node = None

        # search for the item we want to remove (data)
        # Note: without the `actual_node is not None` it will be an inf loop
        # the while loop only serve as the SEARCH function
        while actual_node is not None and actual_node.data != data:
            # current node is not what we look for then move on and set it as previous node
            previous_node = actual_node
            # pointing to the next node
            actual_node = actual_node.next_node

        # search miss: if data not in linked list at all
        if actual_node is None:
            return

        # the head node is the one we want to remove
        if previous_node is None:
            # if we remove the head node then the new head will be the previous
            # 12 -> 4 -> 123 ==> 4 -> 123
            self.head = actual_node.next_node
        else:
            # remove an internal node by updating the pointers
            # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
            """
            if we wanna remove 4:
            12 -> 4 (actual) -> 123 ===> 12 -> 123
            previous_node(12).next_node -> actual_node(4).next_node = 123
            """
            previous_node.next_node = actual_node.next_node

        # MAKE SURE TO REDUCE size of the linked list after removal
        self.num_of_nodes -= 1


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert_start(1)
    linked_list.insert_start(2)
    linked_list.insert_start(3)
    linked_list.insert_start(4)
    linked_list.insert_end(5)

    linked_list.remove(3)

    linked_list.traverse()
