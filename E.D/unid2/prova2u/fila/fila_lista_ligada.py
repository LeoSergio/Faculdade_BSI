class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node

    def dequeue(self):
        if self.front is None:
            return None
        valor = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return valor

    def is_empty(self):
        return self.front is None
