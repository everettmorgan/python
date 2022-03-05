import random
import uuid
from enum import Enum


class Node:
    def __init__(self, data):
        self.id = uuid.uuid4()
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.id}> {self.data}'


def perfect_binary_tree():
    a = Node(4)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(5)
    g = Node(7)

    a.left = b
    a.right = c
    a.parent = None

    b.parent = a
    b.left = d
    b.right = e

    c.parent = a
    c.left = f
    c.right = g

    d.parent = b
    d.left = None
    d.right = None

    e.parent = b
    e.left = None
    e.right = None

    f.parent = c
    f.left = None
    f.right = None

    g.parent = c
    g.left = None
    g.right = None

    return a


def insert(node, data, height=0):
    def new(x):
        new_node = Node(x)
        new_node.parent = node
        new_node.height = height + 1
        return new_node

    # go left if data is smaller than root node
    if node.data >= data:
        # set the left node if the spot is open
        if node.left is None:
            node.left = new(data)
        # otherwise, recursively walk down the left tree
        else:
            insert(node.left, data, height + 1)
    # otherwise, go right
    else:
        # set the right node if the spot is open
        if node.right is None:
            node.right = new(data)
        # otherwise, recursively walk down the right tree
        else:
            insert(node.right, data, height + 1)


def print_perfect_binary_tree(node, height=0):
    if node is not None:
        print_perfect_binary_tree(node.right, height + 1)
        print(' ' * 4 * height, node.data)
        print_perfect_binary_tree(node.left, height + 1)


def preorder_perfect_tree_traversal(node):
    """
    node, left, right
    """
    print(node.data)

    if node.left is not None:
        preorder_perfect_tree_traversal(node.left)
    if node.right is not None:
        preorder_perfect_tree_traversal(node.right)


if __name__ == '__main__':
    tree = perfect_binary_tree()

    print_perfect_binary_tree(tree)

    preorder_perfect_tree_traversal(tree)
