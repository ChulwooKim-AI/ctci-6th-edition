"""Route Between Nodes 

Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

Hints: 
#127
Two well-known algorithms can do this. What are the tradeoffs between them?
"""

from collections import defaultdict
import unittest

def is_route(graph, node1, node2, mode="bfs"):
    if mode == "bfs":
        return bfs(graph, node1, node2)
    elif mode == "dfs":
        return dfs(graph, node1, node2)
    else:
        return None

def bfs(graph, departure, destination):
    if departure == destination:
        return True
    visited = []
    queue = [departure]

    while queue:
        node = queue.pop(0)        
        if node not in visited:
            visited.append(node)
            for edge in graph[node]:                        
                if edge == destination:
                    return True
                queue.append(edge)                
    return False

def dfs(graph, departure, destination):    
    path = __dfs(graph, departure, visited=[])    
    return True if destination in path else False

def __dfs(graph, departure, visited):    
    visited.append(departure)
    for edge in graph[departure]:        
        if edge not in visited:
            visited = __dfs(graph, edge, visited)
    return visited
    

class Test(unittest.TestCase):
    def setUp(self):
        self.graph = defaultdict(list)
        self.graph[0].append(1)
        self.graph[0].append(3)
        self.graph[1].append(2)
        self.graph[1].append(4)
        self.graph[2].append(5)
        self.graph[5].append(3)
        self.graph[3].append(4)
        self.graph[4].append(2)
    
    def test_bfs(self):
        self.assertTrue(is_route(self.graph, 0, 4))
        self.assertTrue(is_route(self.graph, 4, 2))
        self.assertTrue(is_route(self.graph, 4, 5))
        self.assertTrue(is_route(self.graph, 4, 3))
        self.assertFalse(is_route(self.graph, 4, 0))

    def test_dfs(self):
        self.assertTrue(is_route(self.graph, 0, 4, mode="dfs"))
        self.assertTrue(is_route(self.graph, 4, 2, mode="dfs"))
        self.assertTrue(is_route(self.graph, 4, 5, mode="dfs"))
        self.assertTrue(is_route(self.graph, 4, 3, mode="dfs"))
        self.assertFalse(is_route(self.graph, 4, 0, mode="dfs"))

if __name__ == "__main__":
    unittest.main()