class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
            
    def insert(self, data):        
        if self.root:            
            self._insert(self.root, data)
        else:
            self.root = Node(data)            
    
    def _insert(self, node, data):
        if node.data < data:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)
        else:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
    
    def show(self):
        if self.root is None:            
            return None              
        return self._pre_order(self.root, path=[])
    
    def _pre_order(self, node, path):
        if node:            
            path.append(node.data)
            self._pre_order(node.left, path)
            self._pre_order(node.right, path)
            return path
                