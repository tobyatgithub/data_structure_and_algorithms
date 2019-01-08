from ...data_structures.node_graph.node_graph import graph, Vertex
from .get_edge import get_edge
import pytest


@pytest.fixture()
def small_graph():
    tmp = graph()
    # tmp.addVertex("Seattle")
    # tmp.addVertex("Boston")
    # tmp.addVertex("New York City")
    # tmp.addVertex("Rochester")
    # tmp.addVertex("Chicago")
    tmp.addTwoWayEdges("Seattle", "Boston", 224)
    tmp.addTwoWayEdges("Seattle", "Chicago", 73)
    tmp.addTwoWayEdges("Seattle", "New York City", 196)
    tmp.addTwoWayEdges("Chicago", "Boston", 185)
    tmp.addTwoWayEdges("Chicago", "Rochester", 120)
    tmp.addTwoWayEdges("Chicago", "New York City", 181)
    tmp.addTwoWayEdges("Boston", "Rochester", 105)
    tmp.addTwoWayEdges("New York City", "Rochester", 99)
    tmp.addTwoWayEdges("Boston", "New York City", 58)
    return tmp


def test_import():
    assert Vertex
    assert graph


def test_get_edge1(small_graph):
    cities = ["Seattle", "Rochester"]
    assert (False, 0) == get_edge(small_graph, cities)


def test_get_edge2(small_graph):
    cities = ["Seattle", "Boston"]
    assert (True, 224) == get_edge(small_graph, cities)


def test_get_edge3(small_graph):
    cities = ["Seattle", "New York City"]
    assert (True, 196) == get_edge(small_graph, cities)


def test_get_edge4(small_graph):
    cities = ["Seattle", "Seattle"]
    assert (False, 0) == get_edge(small_graph, cities)

def test_get_edge5(small_graph):
    cities = ["Seattle"]
    assert (False, 0) == get_edge(small_graph, cities)
