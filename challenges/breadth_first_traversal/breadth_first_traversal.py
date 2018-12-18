# from ...data_structures.queue.queue import Queue
# having issues with Queue...@_@

def breadth_first_traversal(in_tree):
    """
    Breadth first traversal method which takes a Binary Tree as its unique input.
    """
    storage = [in_tree.root]
    # current = in_tree.root
    # storage = []
    # if current:
    #     storage.append(current)
    # debug_res = []
    while len(storage) > 0:
        current = storage.pop(0)
        print(current.val)
        # debug_res.append(current.val)
        if current.left:
            storage.append(current.left)
        if current.right:
            storage.append(current.right)

    # import pdb; pdb.set_trace()
    # return debug_res
    return True

