# import sys
# # import via absolute directory.
# sys.path.append('/Users/toby/Documents/seattle-python-401d10/'
# 'data_structure_and_algorithms/data_structures/stack')

# from stack import Stack
from ...data_structures.stack.stack import Stack

class PseudoQueue(object):
    """
    """

    def __init__(self):
        # self.head = None
        self.stack_Enq = Stack()
        self.stack_Deq = Stack()
        self._size = 0



    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        return self._size

    def enqueue(self, val):
        """
        inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        if not val:
            raise TypeError('Enqueue needs 1 input value, None given.')
        # make sure dequeue backet is empty
        while self.stack_Deq.peek() is not None:
            self.stack_Enq.push(self.stack_Deq.pop())
        self.stack_Enq.push(val)
        self._size += 1

    def dequeue(self):
        """
        extracts a value from the PseudoQueue, using a first-in, first-out approach.
        """

        # make sure enqueue backet is empty
        while self.stack_Enq.peek() is not None:
            self.stack_Deq.push(self.stack_Enq.pop())
        self._size -= 1
        return self.stack_Deq.pop()



