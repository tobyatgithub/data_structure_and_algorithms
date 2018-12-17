import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        out = f'This is a tree node with value = { self.val } and left = { self.left } and right = { self.right }'
        return out

    def __repr__(self):
        out = f'This is a tree node with value = { self.val } and left = { self.left }'
        f'and right = { self.right }'
        return out

class BST:
    def __init__(self, iterable = []):
        self.root = None

        if iterable:
            if isinstance(iterable, collections.Iterable):
                for i in iterable:
                    self.insert(i)
            else:
                raise TypeError(f'BST shall take None or Iterable value as input, { iterable } given')


    def __str__(self):
        out = f'This is a binay search tree with root = { self.root.val }'
        return out

    def __repr__(self):
        return f'This is a binay search tree with root = { self.root.val }'

    def insert(self, val):
        """
        """

        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def preOrder(self, root):
        """
        """
        if root:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        """post order = visit the current node after its child nodes"""
        if root:# if current node not empty
            #1. check left child exist, if so, go to it
            if root.left:
                self.postOrder(root.left)
            #2. if left child finished, check right child
            if root.right:
                self.postOrder(root.right)
            #3. if both finished, print self.
            print(root.val)

    def inOrder(self, root):
        """in order = print left, node, then right"""
        if root:
            if root.left:
                self.inOrder(root.left)

            print(root.val)
            if root.right:
                self.inOrder(root.right)
