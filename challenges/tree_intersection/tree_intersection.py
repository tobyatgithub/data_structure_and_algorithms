"""
In this file, we write a function called tree_intersection that
takes two binary tree parameters. Without utilizing any of the
built-in library methods available to your language, return a
set of values found in both trees.
"""


def tree_intersection(tree1, tree2):
    """
    This function takes in two binary trees as input,
    read the first tree and store everything into a
    dictionary.
    Traverse the second tree and compare. (notice that
    we don't store data of second tree.)
    """
    store = {}

    def preOrder1(tree, root, storage={}):
        """
        Traverse tree 1
        """
        if root:
            value = root.val
            storage.setdefault(value, 0)
            storage[value] += 1
            preOrder1(tree, root.left, storage=storage)
            preOrder1(tree, root.right, storage=storage)

    preOrder1(tree1, tree1.root, store)

    duplicate = []

    def preOrder2(tree, root, storage):
        """
        Traverse tree 2 and compare
        """
        if root:
            value = root.val
            if value in storage.keys():
                duplicate.append(value)
            else:
                storage.setdefault(value, 0)
            storage[value] += 1

            preOrder2(tree, root.left, storage)
            preOrder2(tree, root.right, storage)

    preOrder2(tree2, tree2.root, store)
    return set(duplicate)
