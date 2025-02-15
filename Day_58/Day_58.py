#Implement a depth-first search (DFS) algorithm.


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)

        for neighbor in graph.get(node, []):
            dfs_recursive(graph, neighbor, visited)

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Recursive Traversal:")
dfs_recursive(graph, 'A')  # Output: A B D E F C
