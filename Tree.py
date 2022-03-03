import random


class Node:
    def __init__(self, data, parent=None, height=0):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        # non-standard properties
        self.path = None  # string representation of the path from root->node (for printing purposes)
        self.height = height  # the height of the node (for printing purposes)

    def __str__(self):
        return f'<{hex(id(self))}> {self.data} ({self.path})'


def __insert(node, data, height=0):
    # go left if data is smaller than root node
    if node.data >= data:
        # if the space is empty, create a node and add it to the tree
        if node.left is None:
            new = Node(data, node, height + 1)
            new.path = f'{node.path}->L'
            node.left = new
        # otherwise, recursively walk down the left tree
        else:
            __insert(node.left, data, height + 1)
    # otherwise, go right
    else:
        # if the space is empty, create a node and add it to the tree
        if node.right is None:
            new = Node(data, node, height + 1)
            new.path = f'{node.path}->R'
            node.right = new
        # otherwise, recursively walk down the right tree
        else:
            __insert(node.right, data, height + 1)


def __walk(node, fn):
    fn(node)
    if node.left is not None:
        __walk(node.left, fn)
    if node.right is not None:
        __walk(node.right, fn)


def __nprint(x):
    tabs = '-|-'*x.height
    print(f'[ {x.height} ] {tabs} {x}')


def walk(node, fn):
    __walk(node, fn)


def insert(node, data):
    __insert(node, data)


def nprint(node):
    __walk(node, lambda x: __nprint(x))


def find(node, data):
    curr = node
    while curr is not None and curr.data != data:
        if curr.data >= data:
            curr = curr.left
        else:
            curr = curr.right
    return curr


if __name__ == '__main__':
    root = Node(125)

    for i in range(50):
        insert(root, random.randrange(250))

    insert(root, 23)

    nprint(root)

    print(find(root, 23))

