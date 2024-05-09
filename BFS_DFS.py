from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                result.append(vertex)
                visited.add(vertex)
                queue.extend(self.graph[vertex])

        return result

    def dfs_util(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, result)

    def dfs(self, start):
        visited = set()
        result = []
        self.dfs_util(start, visited, result)
        return result

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS Traversal:", g.bfs(2))
print("DFS Traversal:", g.dfs(2))