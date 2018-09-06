"""Animal Shelter

An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure.

Hints: 
#22
We could consider keeping a single linked list for dogs and cats, and then iterating
through it to find the first dog (or cat). What is the impact of doing this?
#56
Let's suppose we kept separate lists for dogs and cats. How would we find the oldest
animal of any type? Be creative!
#63
Think about how you'd do it in real life. You have a list of dogs in chronological order and
a list of cats in chronological order. What data would you need to find the oldest animal?
How would you maintain this data?
"""

import unittest

class Node:
    def __init__(self, order=None, next=None):
        self.order = order
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, order):
        new_node = Node(order)
        
        if not self.tail:        
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def remove(self):        
        value = self.head.order
        self.head = self.head.next
        return value

    def get_oldest_one(self):
        if self.head is None:
            return None
        return self.head.order
        
    def show(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.order) + " -> "
            current_node = current_node.next
        result += "None"
        return result


class AnimalShelter:
    def __init__(self):
        self.dogs_list = LinkedList()
        self.cats_list = LinkedList()
        self.total_order = 0
    
    def enqueue(self, data):
        self.total_order += 1
        if data == "dog":
            self.dogs_list.append(self.total_order)
        elif data == "cat":
            self.cats_list.append(self.total_order)
    
    def dequeueAny(self):
        if self.dogs_list.get_oldest_one() is None and self.cats_list.get_oldest_one() is None:
            return "There are no animals here"
        elif self.dogs_list.get_oldest_one() is None:
            self.cats_list.remove()
            return "You got a cat"
        elif self.cats_list.get_oldest_one() is None:
            self.dogs_list.remove()
            return "You got a dog"
        if self.dogs_list.get_oldest_one() < self.cats_list.get_oldest_one():
            self.dogs_list.remove()
            return "You got a dog"
        else:
            self.cats_list.remove()
            return "You got a cat"
    
    def dequeueDog(self):
        if self.dogs_list.get_oldest_one() is None:
            return "There are no dogs here"
        self.dogs_list.remove()
        return "You got a dog"
    
    def dequeueCat(self):
        if self.cats_list.get_oldest_one() is None:
            return "There are no cats here"
        self.cats_list.remove()
        return "You got a cat"

class Test(unittest.TestCase):
    def setUp(self):
        self.shelter = AnimalShelter()
        self.shelter.enqueue("dog")
        self.shelter.enqueue("dog")
        self.shelter.enqueue("cat")
        self.shelter.enqueue("cat")
        self.shelter.enqueue("dog")
        self.shelter.enqueue("cat")
    
    def test_leave(self):
        self.assertEqual(self.shelter.dequeueAny(), "You got a dog")
        self.assertEqual(self.shelter.dequeueCat(), "You got a cat")
        self.assertEqual(self.shelter.dequeueAny(), "You got a dog")
        self.assertEqual(self.shelter.dequeueAny(), "You got a cat")
        self.assertEqual(self.shelter.dequeueDog(), "You got a dog")
        self.assertEqual(self.shelter.dequeueDog(), "There are no dogs here")
        self.assertEqual(self.shelter.dequeueAny(), "You got a cat")
        self.assertEqual(self.shelter.dequeueAny(), "There are no animals here")
        

if __name__ == "__main__":
    unittest.main()