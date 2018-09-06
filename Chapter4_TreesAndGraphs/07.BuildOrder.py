"""Build Order

You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.

EXAMPLE
Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c

Hints: 
#26
Build a directed graph representing the dependencies. Each node is a project and an
edge exists from A to B if B depends on A (A must be built before B). You can also build
it the other way if it's easier for you.
#47
Look at this graph. Is there any node you can identify that will definitely be okay to build
first?
#60
If you identify a node without any incoming edges, then it can definitely be built. Find
this node (there could be multiple) and add it to the build order. Then, what does this
mean for its outgoing edges?
#85
Once you decide to build a node, its outgoing edge can be deleted. After you've done
this, can you find other nodes that are free and clear to build?
#125
As a totally different approach: Consider doing a depth-first search starting from an arbitrary
node. What is the relationship between this depth-first search and a valid build
order?
#133
Pick an arbitrary node and do a depth-first search on it. Once we get to the end of a path,
we know that this node can be the last one built, since no nodes depend on it. What
does this mean about the nodes right before it?

Comment:
This is a question about a topological sort. 
A topological sort takes a directed acyclic graph and produces a linear ordering of all its vertices 
such that if the graph G contains an edge (v,w) then the vertex v comes before the vertex w in the ordering. 
Directed acyclic graphs are used in many applications to indicate the precedence of events. 
Making pancakes is just one example; other examples include software project schedules, 
precedence charts for optimizing database queries, and multiplying matrices.
"""

from collections import defaultdict
import unittest

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_vertex(self, vertex):
        self.graph[vertex] = []
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def get_vertice(self):
        result = []
        for x in self.graph.keys():
            result.extend(x)        
        return  result

    def build_order(self):
        stack = []
        visited = []
        for vertex in self.get_vertice():
            if vertex not in visited:
                self.__topological_sort(visited, vertex, stack)            
        return stack

    def __topological_sort(self, visited, vertex, stack):
        visited.append(vertex)
        for edge in self.graph[vertex]:
            if edge not in visited:
                self.__topological_sort(visited, edge, stack)        
        stack.insert(0, vertex)


class Test(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex("a")
        self.graph.add_vertex("b")
        self.graph.add_vertex("c")
        self.graph.add_vertex("d")
        self.graph.add_vertex("e")
        self.graph.add_vertex("f")        
        self.graph.add_edge("a", "d")
        self.graph.add_edge("f", "b")
        self.graph.add_edge("b", "d")
        self.graph.add_edge("f", "a")
        self.graph.add_edge("d", "c")
    
    def test_build_order(self):
        self.assertEqual(self.graph.build_order(), ["f", "e", "b", "a", "d", "c"])

if __name__ == "__main__":
    unittest.main()