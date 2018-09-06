from collections import defaultdict

class Vertex:
    def __init__(self, data=None):
        self.data = data
        self.adjacent_data = defaultdict(list)
        self.visited = False

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)                
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)        
    
    def get_values(self):
        result = []
        for x in self.graph.values():
            result.extend(x)
        return  result

    def dfs(self, vertex, visited=[]):
        visited.append(vertex)
        for edge in self.graph[vertex]:
            if edge not in visited:
                self.dfs(edge, visited)
        return visited
    
    def dfs_with_stack(self, start_vertex):
        visited = []
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)                
                for edge in self.graph[vertex]:
                    stack.append(edge)        
        return visited
 
    def bfs(self, start_vertex):
        visited = []
        queue = [start_vertex]
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                for edge in self.graph[vertex]:
                    queue.append(edge)
        return visited



import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(3, 2)
        self.graph.add_edge(0, 4)
        self.graph.add_edge(4, 5)
        
     

    def test_dfs(self):        
        self.assertEqual(self.graph.dfs(0), [0, 1, 2, 3, 4, 5])
    
    def test_dfs_with_stack(self):        
        self.assertEqual(self.graph.dfs_with_stack(0), [0, 4, 5, 2, 3, 1])
    
    def test_bfs(self):
        self.assertEqual(self.graph.bfs(0), [0, 1, 2, 4, 3, 5])

if __name__ == "__main__":
    unittest.main()