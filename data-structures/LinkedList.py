def addr(thing):
    return hex(id(thing)) if thing is not None else 'None'


class Node:
    """
    a standard circular Node implementation
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Node<{addr(self)}>: data={self.data} next={addr(self.next)} prev={addr(self.prev)}'


class LinkedList:
    """
    a standard circular LinkedList implementation
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if node == self.head:
            if node.next is not None and node.prev is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.head = node.next
            else:
                self.head = None
        else:
            if node.next is not None and node.prev is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
            elif node.next is None:
                node.prev.next = None
            elif node.prev is None:
                node.next.prev = None

    def purge(self, data):
        """
        removes all Nodes where Nodes.data == data
        """
        curr = self.find(data)

        while curr is not None:
            self.remove(curr)
            curr = self.find(data)

    def find(self, data):
        """
        finds and returns the first Node where Node.data == data
        """
        out = 0
        curr = self.head

        while curr.data != data and out == 0:
            curr = curr.next
            if curr == self.head:
                out = 1

        return curr if curr is not None and curr.data == data else None

    def pop(self):
        """
        removes the topmost Node from the LinkedList
        """
        if self.head is None:
            return
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next

    def push(self, data):
        """
        creates and pushes a new Node into the LinkedList
        """
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

        if self.tail is None:
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail

    def print(self, newline=False):
        """
        prints a linked list in its entirety
        """
        out = 0
        curr = self.head
        while curr is not None and out == 0:
            print(curr)
            curr = curr.next
            if curr is self.head:
                out = 1
        print('\n')


if __name__ == '__main__':
    ll = LinkedList()

    ll.push(1)
    ll.push(2)
    ll.push(2)
    ll.push(3)
    ll.push(3)
    ll.push(3)
    ll.push(3)
    ll.push(4)
    ll.push(4)
    ll.push(5)
    ll.push(5)
    ll.push(5)
    ll.push(6)
    ll.push(6)
    ll.push(6)
    ll.push(6)

    ll.print()

    # Node<0x10e735f70>: data=6 next=0x10e735f10 prev=0x10e6d8820
    # Node<0x10e735f10>: data=6 next=0x10e735eb0 prev=0x10e735f70
    # Node<0x10e735eb0>: data=6 next=0x10e735e50 prev=0x10e735f10
    # Node<0x10e735e50>: data=6 next=0x10e735df0 prev=0x10e735eb0
    # Node<0x10e735df0>: data=5 next=0x10e735dc0 prev=0x10e735e50
    # Node<0x10e735dc0>: data=5 next=0x10e735d00 prev=0x10e735df0
    # Node<0x10e735d00>: data=5 next=0x10e735ca0 prev=0x10e735dc0
    # Node<0x10e735ca0>: data=4 next=0x10e735c40 prev=0x10e735d00
    # Node<0x10e735c40>: data=4 next=0x10e735be0 prev=0x10e735ca0
    # Node<0x10e735be0>: data=3 next=0x10e735b80 prev=0x10e735c40
    # Node<0x10e735b80>: data=3 next=0x10e6f5f10 prev=0x10e735be0
    # Node<0x10e6f5f10>: data=3 next=0x10e6f5ee0 prev=0x10e735b80
    # Node<0x10e6f5ee0>: data=3 next=0x10e6f59a0 prev=0x10e6f5f10
    # Node<0x10e6f59a0>: data=2 next=0x10e6f5640 prev=0x10e6f5ee0
    # Node<0x10e6f5640>: data=2 next=0x10e6d8820 prev=0x10e6f59a0
    # Node<0x10e6d8820>: data=1 next=0x10e735f70 prev=0x10e6f5640

    ll.purge(4)

    ll.remove(ll.find(5))
    ll.remove(ll.find(5))
    ll.remove(ll.find(5))

    ll.print()

    # Node<0x10e735f70>: data=6 next=0x10e735f10 prev=0x10e6d8820
    # Node<0x10e735f10>: data=6 next=0x10e735eb0 prev=0x10e735f70
    # Node<0x10e735eb0>: data=6 next=0x10e735e50 prev=0x10e735f10
    # Node<0x10e735e50>: data=6 next=0x10e735be0 prev=0x10e735eb0
    # Node<0x10e735be0>: data=3 next=0x10e735b80 prev=0x10e735e50
    # Node<0x10e735b80>: data=3 next=0x10e6f5f10 prev=0x10e735be0
    # Node<0x10e6f5f10>: data=3 next=0x10e6f5ee0 prev=0x10e735b80
    # Node<0x10e6f5ee0>: data=3 next=0x10e6f59a0 prev=0x10e6f5f10
    # Node<0x10e6f59a0>: data=2 next=0x10e6f5640 prev=0x10e6f5ee0
    # Node<0x10e6f5640>: data=2 next=0x10e6d8820 prev=0x10e6f59a0
    # Node<0x10e6d8820>: data=1 next=0x10e735f70 prev=0x10e6f5640
