
class Queue:

    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    # O(1) running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time but we could use doubly linked list since it can manipulate 1st/last item in o(1)
    # to achieve O(1) for all operations
    # since we remove the 1st item,the rest of items in the array has to shift leftward --> O(N)
    def dequeue(self):
        # ensure that dequeue is stopped once the queue is empty
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        return None

    # O(1) constant running time
    def peek(self):
        return self.queue[0]

    # O(1)
    def size_queue(self):
        return len(self.queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Size: {q.size_queue()}")
    print(f"Pop: {q.dequeue()}")
    print(f"Peek: {q.peek()}")
