#Implement a depth-first search (DFS) algorithm.


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))  # Reverse to maintain order

# Example Usage
print("\nDFS Iterative Traversal:")
dfs_iterative(graph, 'A')  # Output: A B D E F C
