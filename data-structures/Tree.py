class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.letter = None

    def __str__(self):
        return f'<{hex(id(self))}> {self.data}'


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
    a.letter = 'A'

    b.parent = a
    b.left = d
    b.right = e
    b.letter = 'B'

    c.parent = a
    c.left = f
    c.right = g
    c.letter = 'C'

    d.parent = b
    d.left = None
    d.right = None
    d.letter = 'D'

    e.parent = b
    e.left = None
    e.right = None
    e.letter = 'E'

    f.parent = c
    f.left = None
    f.right = None
    f.letter = 'F'

    g.parent = c
    g.left = None
    g.right = None
    g.letter = 'G'

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
        print(' ' * 8 * height, node.data, f'({node.letter})')
        print_perfect_binary_tree(node.left, height + 1)


def preorder_perfect_tree_recursive(node, fn=print):
    """
    node, left, right
    """
    fn(node)

    if node.left is not None:
        preorder_perfect_tree_recursive(node.left, fn)
    if node.right is not None:
        preorder_perfect_tree_recursive(node.right, fn)


def preorder_perfect_tree_corecursive(node, fn=print):
    """
    node, left, right
    """
    stk = []
    curr = node

    while True:
        while curr is not None:
            fn(curr)
            stk.append(curr)
            curr = curr.left

        if len(stk) == 0:
            return

        curr = stk.pop()
        curr = curr.right


def breadth_first_perfect_tree_corecursive(node, fn=print):
    curr = node
    stk = []

    while True:
        while curr is not None:
            fn(curr)
            if curr.left is not None:
                stk.append(curr.left)
            if curr.right is not None:
                stk.append(curr.right)
            if len(stk) == 0:
                return
            curr = stk.pop(0)


def inorder_perfect_tree_corecursive(node, fn=print):
    curr = node
    stk = []

    # get to start (leftmost + highest node)
    while curr.left is not None:
        curr = curr.left

    while True:
        while curr is not None:
            fn(curr)
            if curr.right is not None:
                stk.insert(0, curr.right)
            elif curr.left is not None:
                stk.insert(0, curr.left)
            if curr.parent is not None:
                stk.insert(0, curr.parent)
            if len(stk) == 0:
                return
            curr = stk.pop()


def print_node(node):
    print(f'    {node.data} ({node.letter})')


if __name__ == '__main__':
    tree = perfect_binary_tree()

    print_perfect_binary_tree(tree)

    print('\n')

    print('PreOrder Traversal [A,B,D,E,C,F,G]')

    print('  (recursive)')
    preorder_perfect_tree_recursive(tree, print_node)

    print('  (corecursive)')
    preorder_perfect_tree_corecursive(tree, print_node)

    print('\n')

    print('BFD Traversal [A,B,C,D,E,F,G]')
    print('  (corecursive)')
    breadth_first_perfect_tree_corecursive(tree, print_node)

    print('In-order Traversal [D,B,E,A,F,C,G]')
    print('  (corecursive)')
    inorder_perfect_tree_corecursive(tree, print_node)

    #                 7(G)
    #         6(C)
    #                 5(F)
    # 4(A)
    #                 3(E)
    #         2(B)
    #                 1(D)
    #
    # PreOrder Traversal [A, B, D, E, C, F, G]
    #     (recursive)
    #         4(A)
    #         2(B)
    #         1(D)
    #         3(E)
    #         6(C)
    #         5(F)
    #         7(G)
    #     (corecursive)
    #         4(A)
    #         2(B)
    #         1(D)
    #         3(E)
    #         6(C)
    #         5(F)
    #         7(G)
    #
    # BFD Traversal [A, B, C, D, E, F, G]
    #     (corecursive)
    #         4(A)
    #         2(B)
    #         6(C)
    #         1(D)
    #         3(E)
    #         5(F)
    #         7(G)
