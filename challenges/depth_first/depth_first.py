from ...data_structures.node_graph.node_graph import graph, Vertex


def explore(in_graph, node):
    """
    This function will take in a node and recursively explore it.
    """
    if not node.visited:
        # print('exploring node ', node.value)
        print(node.value, end='')
        node.visited = True
        for n in node.getNeighbor():
            tmp = in_graph.getVertex(n)
            explore(in_graph, tmp)


def depth_first(in_graph, start, init_graph=True, end_clean_graph=False):
    """
    In this function, we implement the depth first traverse of a graph.
    We can use a stack or use recursive techniques to achieve that.
    Notice that stack approach will take extra space, but the recursive
    one won't.

    For the code below, we show how to do this in recursive way.
    """
    # init graph visit status
    if init_graph:
        in_graph.search_helper()

    explore(in_graph, start)

    # end re-init graph visit status
    if end_clean_graph:
        in_graph.search_helper()

