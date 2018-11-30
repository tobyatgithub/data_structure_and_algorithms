from node import Node


class linked_list(object):
    """
    A Linked List is a sequence of Nodes that are connected/linked to each other.
    The most defining feature of a linked List is that each Node references the
    next Node in the link.
    """

    def __init__(self, iterable = []):
        # iterable allows you to pass in a list
        self.head = None
        self._size = 0

        # iterable has to be a list (or at least immutable),
        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for i in iterable:
            self.insert(i)

    def __str__(self):
        output = f'Linked List: Head val - { self.head }'
        return output

    def __repr__(self):
        output = f'<LinkedList: head - { self.head }, size - { self._size }>'
        return output

    def __len__(self):
        return self._size

    def insert(self, val):
        """
        This function takes any value as input and add this value as a node instance
        into the head location of the linked list, and make this new insertion the new
        head.
        input: value, can be in any type (*)
        output: update the linked list inplace. (self.head, self._size)
        """

        new_node = Node(val)
        new_node._next = self.head
        self.head = new_node

        # self.head = Node(val, self.head)

        self._size += 1

    def includes(self, target):
        """
        This function takes any value as an argument and returns True or False
        depending on whether that value exists as a Node value within the list.
        input: a target value, could be anything (*)
        output: True of False whether this linkedlist contain this target value (boolean)
        """

        # if the linked list is empty, there won't be any value
        if self.head is None:
            return False

        while self.head is not None:
            if target == self.head.val:
                return True
            self.head = self.head._next
        return False

