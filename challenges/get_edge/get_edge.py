from ...data_structures.node_graph.node_graph import graph, Vertex


def get_edge(in_graph, in_list):
    """
    This function takes in a graph, and an array of city names.
    Return whether the full trip is possible with direct flights,
    and how much it would cost.
    """
    total = 0
    if len(in_list) <= 1:
        return False, 0

    for i in range(0, len(in_list) - 1):
        from_city = in_graph.getVertex(in_list[i])
        to_city = in_graph.getVertex(in_list[i+1])
        path_exist = to_city.value in from_city.getNeighbor()
        # import pdb; pdb.set_trace()
        if path_exist:
            weight = from_city.getWeight(to_city.value)
            total += weight
        else:
            return False, 0

    return True, total


