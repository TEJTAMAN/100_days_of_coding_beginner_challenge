#Implement a linked list.


class Node:
    """A simple Node class for Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A basic Linked List implementation"""
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end"""
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def delete(self, key):
        """Delete a node by value"""
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev, current = current, current.next

        if current:
            prev.next = current.next

    def search(self, key):
        """Search for a node"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """Print the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
ll = LinkedList()
for value in [10, 20, 30, 40]:
    ll.insert(value)

ll.display()  # Output: 10 -> 20 -> 30 -> 40 -> None

ll.delete(20)
ll.display()  # Output: 10 -> 30 -> 40 -> None

print("Search 30:", ll.search(30))  # Output: True
print("Search 50:", ll.search(50))  # Output: False
