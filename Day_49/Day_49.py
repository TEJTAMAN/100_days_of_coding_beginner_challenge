#Implement a binary search tree.


class Node:
    """A class representing a node in a Binary Search Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        """Helper method for inserting recursively."""
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        """Helper method for searching recursively."""
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    def inorder_traversal(self):
        """Perform an inorder traversal (Left -> Root -> Right)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        """Helper method for inorder traversal."""
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.value)
            self._inorder_recursive(current.right, result)

    def min_value(self):
        """Find the minimum value in the BST."""
        current = self.root
        while current and current.left:
            current = current.left
        return current.value if current else None

    def max_value(self):
        """Find the maximum value in the BST."""
        current = self.root
        while current and current.right:
            current = current.right
        return current.value if current else None


# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)

    print("Inorder Traversal:", bst.inorder_traversal())  # Should be sorted
    print("Search 40:", bst.search(40))  # True
    print("Search 90:", bst.search(90))  # False
    print("Minimum value:", bst.min_value())  # 20
    print("Maximum value:", bst.max_value())  # 80
