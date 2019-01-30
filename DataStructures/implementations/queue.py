# -*- coding: utf-8 -*-
"""This module implements a Queue using python lists"""
class Queue:
    """Initialize Queue with an element or it defaults to None"""
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        """Inserts a new element at the end of the Queue"""
        return self.storage.append(new_element)

    def peek(self):
        """Returns first element in Queue"""
        return self.storage[0]

    def dequeue(self):
        """Removes and returns first element of Queue"""
        return self.storage.pop(0)
