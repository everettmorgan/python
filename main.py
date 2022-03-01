import pprint


def addr(thing):
    if thing is None:
        return 'None'
    else:
        return hex(id(thing))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Node<{addr(self)}>: data={self.data} next={addr(self.next)} prev={addr(self.prev)}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def purge(self, data):
        curr = self.find(data)

        while curr is not None:
            self.remove(curr)
            curr = self.find(data)

    def remove(self, node):
        if type(node) is Node:
            raise Exception(f'Expected Node, received {type(node)}')
        else:
            if node == self.head:
                self.head = None
            else:
                if node.next is not None:
                    node.next.prev = node.prev if node.prev is not None else None
                if node.prev is not None:
                    node.prev.next = node.next if node.next is not None else None

    def find(self, data):
        curr = self.head
        while curr is not None and curr.data != data:
            curr = curr.next;
        return curr

    def pop(self):
        if self.head is None:
            return
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next

    def push(self, data):
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
        pos = 1
        curr = self.head
        while curr is not None:
            print(curr)
            curr = curr.next
            pos += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(1)

    ll.push(2)
    ll.push(2)
    ll.push(2)
    ll.push(2)

    ll.push(3)

    # ll.purge(2)

    ll.print()
