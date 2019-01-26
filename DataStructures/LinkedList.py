# Implementing a Linked List
class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        Adds a new element to the end of the list
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position. Assume the first
        position is "1". Return None if position is not in the list"""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if position == counter:
                return current
            counter += 1
            current = current.next
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        """Insert new element as the head of the linked list"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first(head) element in the linked list and return it"""
        deleted_element = self.head
        if self.head:
            self.head = self.head.next
            deleted_element.next = None
        return deleted_element