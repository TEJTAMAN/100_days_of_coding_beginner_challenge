#Implement a queue data structure.


class Queue:
    """A simple queue implementation using a list."""
    
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        return self.queue.pop(0)

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)

    def display(self):
        """Print the queue."""
        print("Queue:", self.queue)


# Example usage:
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()

    print(f"Front element: {q.front()}")
    
    print(f"Dequeued: {q.dequeue()}")
    q.display()

    print(f"Queue size: {q.size()}")
    print(f"Is queue empty? {q.is_empty()}")