def addr(thing):
    if thing is None:
        return 'None'
    else:
        return hex(id(thing))


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

    def remove(self):
        """
        removes any next or prev references, and thus itself
        """
        if self.next is not None and self.prev is not None:
            self.next.prev = self.prev
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = None
        if self.prev is not None:
            self.prev.next = None
        self.prev = None
        self.next = None


class LinkedList:
    """
    a standard circular LinkedList implementation
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def purge(self, data):
        """
        removes all Nodes where Nodes.data == data
        """
        curr = self.find(data)

        while curr is not None and curr.data == data:
            curr.remove()
            curr = self.find(data)

    def find(self, data):
        """
        finds and returns the first Node where Node.data == data
        """
        curr = self.head
        while curr is not None and curr.data != data:
            curr = curr.next;
        return curr

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

    def print(self):
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

    ll.purge(4)

    ll.print()
