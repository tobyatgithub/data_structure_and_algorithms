from ...data_structures.node_graph.node_graph import graph, Vertex
from .depth_first import depth_first
import pytest

@pytest.fixture()
def small_graph():
    tmp = graph()
    tmp.addTwoWayEdges("A", "B", 224)
    tmp.addTwoWayEdges("B", "E", 73)
    tmp.addTwoWayEdges("B", "C", 196)
    tmp.addTwoWayEdges("E", "G", 185)
    tmp.addTwoWayEdges("C", "F", 120)
    tmp.addTwoWayEdges("C", "H", 181)
    tmp.addTwoWayEdges("C", "D", 105)
    tmp.addTwoWayEdges("D", "H", 99)
    # tmp.addTwoWayEdges("D", "I", 58)
    return tmp


def test_import():
    assert Vertex
    assert graph


def test_depth_first1(capsys, small_graph):
    A = small_graph.getVertex("A")
    depth_first(small_graph, A)
    captured = capsys.readouterr()
    assert 'ABEGCFHD' in captured.out


def test_depth_first2(capsys, small_graph):
    B = small_graph.getVertex("B")
    depth_first(small_graph, B)
    captured = capsys.readouterr()
    assert 'BAEGCFHD' in captured.out


def test_depth_first3(capsys, small_graph):
    C = small_graph.getVertex("C")
    depth_first(small_graph, C)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert 'CBAEGFHD' in captured.out
