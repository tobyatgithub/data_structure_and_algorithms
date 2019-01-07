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
        out = f'This is a binay search tree with root = { self.root.val }'
        return out

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
            if root.left:
                self.preOrder(root.left)
            if root.right:
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

    def find_maximum_value(self):
        """
        this function takes in a binary tree as input, and return
        the maximum value within the tree as output.
        There are two ways of doing that, one is modify the tree class such that
        we add one .max_val to the self. And modifying the insert process accordingly.
        The other one is to use any kind of traverse to visit every single node in
        the tree, and find out the one with maximum value
        """

        if self.root:
            max_val = self.root.val
            store = [self.root]
            while len(store) > 0:
                cur = store.pop(0)
                if cur.val > max_val:
                    max_val = cur.val
                if cur.right:
                    store.append(cur.right)
                if cur.left:
                    store.append(cur.left)
            return max_val

        print("Empty tree has no maximum value")
        return None

    def kth_Smallest(self, k):
        """
        :type k: int
        :rtype: int
        """
        if self.root:
            # init
            k_list = []

            # breadth first traverse
            queue = [self.root]
            while len(queue) > 0:
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

                # if len of k_list is shorter than k
                if len(k_list) < k:
                    k_list.append(current.val)

                # when k_list has k element, we start to compare and replace
                else:
                    if current.val < max(k_list):
                        k_list[k_list.index(max(k_list))] = current.val

            # finished while loop, select the kth smallest, which is the last one from sorted k_list
            return sorted(k_list)[-1]

        else:
            print("Bad input tree")
            return None




