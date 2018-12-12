from .node import Node
from queue import Queue

# class dog(Node):
class dog(object):
    def __init__(self, name=None, breed=None, color=None, favfood=None):
        # Node.val = 'dog'
        self.val = 'dog'
        self.name = name
        self.breed = breed
        # self.color = color
        # self.favfood = favfood
        # return self

class cat(object):
# class cat(Node):
    def __init__(self, name=None, kind=None, color=None, favfood=None):
        # Node.val = 'cat'
        self.val = 'cat'
        self.name = name
        self.kind = kind
        # self.color = color
        # self.favfood = favfood
        # return self

class AnimalShelter(object):
    """
    The animal shelter class that holds only dogs and cats.
    The shelter operates using a first-in, first-out approach.
    """

    def __init__(self):
        self.front = None
        self.back = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        return self.val

    def __repr__(self):
        return self.val

    def enqueue(self, animal):
        """
        This function adds animal to the shelter. animal can be either
        a dog or a cat object.
        """
        new_node = Node(animal)
        if (self.front is None) and (self.back is None):
            self.front = new_node
            self.back = new_node

        else:
            self.back._next = new_node
            self.back = new_node
        self._size += 1

    def dequeue(self, pref):
        """
        We gonna do dequeue by 5 steps -
        1. check single element case
        2. check the head, 3. check the body, 4, check the tail.
        5. empty or not found case.
        6. case where pref = None
        (bcz each of those 3 parts require different management of the queue)
        """
        self._size -= 1
        # 6. pref = None, or bad input
        if (pref is None) or not ((pref.lower() == 'cat') or (pref.lower() == 'dog')):
            # for now let's return None... just realized this will depends on queue condition as well..!
            print("Please specify whether you prefer cat of dog.")
            return None
            # # return the first on in the animal shelter (queue)
            # lucky = self.head
            # self.head = lucky._next
            # lucky._next = None
            # return lucky

        # 5.1 if empty queue
        if self.head is None:
            print("There's currently no animal in our shelter!")
            return None

        # 1. if single element queue
        if self._size == 1:
            # found
            if self.head.val == pref.lower():
                lukcy = self.head
                # re_init the queue
                self.head = None
                self.back = None
                return lucky
            # not found
            else:
                # print(f"We don't have { pref } in our shelter. Sorry~")
                print("There's currently no preferred animal in our shelter!")
                return None

        # more than one element in queue
        # 2. check the head, it's different from single element case because of tail.
        if pref.lower() == self.head.val:
            lucky = self.head
            self.head = lucky._next
            lucky._next = None
            return lukcy

        # 3. check the body, no head or tail re-wire will be required.
        prev = self.head
        current = self.head._next
        future = self.head._next._next
        while future: # this will lead us to the last node if not returned
            # check and return
            if current.val == pref.lower():
                lucky = current
                prev._next =future
                lucky._next = None
                return lucky
            prev = current
            ccurrent = future
            future = future._next

        # 4. check the tail, will get to this point if we didn't find preferred animal from
        # head, or body. now we check tail. Here current = self.tail., prev._next = current
        if current.val == pref.lower():
            self.tail = prev
            prev._next = None
            return current

        # just in case...
        print("some case failed to catch...please check the code.")
        return None
