"""This module implements a binary tree using nodes and references"""

class BinaryTree:
    """Initializes a binary tree"""
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """Inserts new node to the left side of the tree"""
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t_emp = BinaryTree(new_node)
            t_emp.left_child = self.left_child
            self.left_child = t_emp

    def insert_right(self, new_node):
        """Inserts new node to the right side of the tree"""
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t_emp = BinaryTree(new_node)
            t_emp.right_child = self.right_child
            self.right_child = t_emp



