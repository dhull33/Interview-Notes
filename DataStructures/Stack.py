# Implementing a Stack using a linked list
from .LinkedList import LinkedList
class Stack:
    """Implements the data structure Stack using a linked list"""
    def __init__(self, top=None):
        self.linked_list = LinkedList(top)

    def push(self, new_element):
        """
        Adds a new element to the top of the stack. The head of the linked
        list needs to be changed when adding a new element
        """
        return  self.linked_list.insert_first(new_element)

    def pop(self):
        """Removes the first element off the top of the stack and returns it"""
        return self.linked_list.delete_first()
