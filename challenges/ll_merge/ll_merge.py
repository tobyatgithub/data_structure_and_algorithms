# from ../../data_structure/linked_list/ import linked_list
# from .. import linked_list
import sys
sys.path.append('/Users/toby/Documents/seattle-python-401d10/data_structure_and_algorithms/data_structures/linked_list')
# sys.path.append('../../data_structure/linked_list')


from linked_list import linked_list
from node import Node
def mergeLists(ll1, ll2):
    """
    """

    # special case, ll1 = ll2 = empty ll
    if (ll1.head is None) and (ll2.head is None):
        return linked_list().head

    if ll1.head is None:
        print("linked list 1 is Empty")
        return ll2.head

    if ll2.head is None:
        print("linked list 2 is Empty")
        return ll1.head

    index1 = ll1.head
    index2 = ll2.head
    new_ll = linked_list()
    new_ll.head = Node()
    current = new_ll.head

    while (index1 is not None) and (index2 is not None):
        print("running...")
#         new_ll.insert(index2.val)
        current._next = Node(index1.val)
        current = current._next
#         new_ll.insert(index1.val)
        current._next = Node(index2.val)
        current = current._next
        index1 = index1._next
        index2 = index2._next

    while index1:
        print("inserting index1 = ", index1.val)
        # new_ll.insert(index1.val)
        # current._next = Node(index1.val)
        # current = current._next
        # index1 = index1._next

        # we only need to add to end once, as
        # the index2 here is changed
        current._next = index1
        break

    while index2:
        print("inserting index2 = ", index2.val)
        # new_ll.insert(index2.val)
        # current._next = Node(index2.val)
        # current = current._next
        # index2 = index2._next

        # we only need to add to end once, as
        # the index2 here is changed
        current._next = index2
        break

    return new_ll.head
