"""Single Linked List

"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def show(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            print("->", end=" ")
            current_node = current_node.next
        print(None)
    
    def values(self):
        current_node = self.head
        result = ""
        while current_node is not None:
            result += str(current_node.data) + " -> "            
            current_node = current_node.next
        result += "None"
        return result

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def remove(self, data):
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
            previous_node = current_node
            current_node = current_node.next
            
