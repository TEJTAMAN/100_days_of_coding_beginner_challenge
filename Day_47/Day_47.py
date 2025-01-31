#Implement a stack data structure.


class Stack:
    """A simple stack implementation using a list."""
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the stack."""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        return self.stack.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)

    def display(self):
        """Print the stack."""
        print("Stack:", self.stack)


# Example usage:
if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.display()

    print(f"Top element: {s.peek()}")
    
    print(f"Popped: {s.pop()}")
    s.display()

    print(f"Stack size: {s.size()}")
    print(f"Is stack empty? {s.is_empty()}")

