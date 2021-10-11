import pytest
from math import inf

from src.graph import Graph


def test_negative_number_of_nodes():
    with pytest.raises(ValueError):
        Graph(-3, 2, [[0, 0, 0], [0, 9, 0]])


def test_negative_number_of_edges():
    with pytest.raises(ValueError):
        Graph(2, -4, [[]])


def test_edges_list_length_should_equals_nb_edges():
    with pytest.raises(ValueError):
        Graph(2, 2, [[0, 0, 0]])


def test_graph_without_node():
    graph_test = Graph(0, 0, [])
    assert len(graph_test.get_adj_matrix()) == 0

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 0


def test_graph_with_one_node():
    graph_test = Graph(1, 0, [])
    assert len(graph_test.get_adj_matrix()) == 1

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 1


def test_graph_with_54_nodes():
    graph_test = Graph(54, 0, [])
    assert len(graph_test.get_adj_matrix()) == 54

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 54


def test_edge_with_invalid_values():
    with pytest.raises(ValueError):
        Graph(2, 1, [[0, 3, 3]])


def test_adj_matrix_correctly_filled():
    graph_test = Graph(3, 2, [[0, 2, 3], [0, 1, 1]])
    graph_test_adj_matrix = graph_test.get_adj_matrix()

    for i in range(3):
        for j in range(3):
            if i == 0 and j == 1:
                assert graph_test_adj_matrix[i][j] == 1
            elif i == 0 and j == 2:
                assert graph_test_adj_matrix[i][j] == 3
            else:
                assert graph_test_adj_matrix[i][j] == inf
