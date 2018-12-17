from ... import node

"""
In this file, we write a function called FizzBuzzTree
which takes a tree as an argument. Without utilizing any
of the built-in methods available to your language,
determine weather or not the value of each node is divisible
by 3, 5 or both, and change the value of each of the nodes:

If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

Return the tree with its news values.
"""


def FizzBuzzTree(in_tree):
    """
    """

    def fizzit(value):
        """
        Need I say more? fizz it!
        input: a value
        output: result acccording to the fizz buzz rule
        """
        if value % 15 == 0:
            return "FizzBuzz"
        if value % 5 == 0:
            return "Buzz"
        if value % 3 == 0:
            return "Fizz"
        return value


    def in_order_traverse(root):
        """
        the helper function such that it takes in a node,
        and then do the fizz buzz tree transform on the node
        according to the preOrder order.
        """
        if root:
            root.val = fizzit(root.val)
            in_order_traverse(root.left)
            in_order_traverse(root.right)


    if in_tree.root:
        in_order_traverse(in_tree.root)
    return in_tree
