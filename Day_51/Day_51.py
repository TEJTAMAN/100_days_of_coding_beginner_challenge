#Implement a graph data structure.


class Graph:
    """A class to represent a graph using an adjacency list"""
    def __init__(self):
        self.graph = {}  # Dictionary to store adjacency list

    def add_vertex(self, vertex):
        """Add a new vertex to the graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices (Undirected Graph)"""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        """Print the adjacency list representation of the graph"""
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, edges))}")

    def bfs(self, start):
        """Breadth-First Search (BFS) traversal"""
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)
        print()

    def dfs(self, start, visited=None):
        """Depth-First Search (DFS) traversal (Recursive)"""
        if visited is None:
            visited = set()
        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)


# Example Usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

print("Graph Representation:")
g.display()

print("\nBFS Traversal from node 1:")
g.bfs(1)

print("\nDFS Traversal from node 1:")
g.dfs(1)
