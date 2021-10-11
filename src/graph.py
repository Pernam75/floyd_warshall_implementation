from math import inf


class Graph:
    """
    Graph represents graph used for floyd-warshall algorithm
    """

    def __init__(self, nb_nodes, nb_edges, edges):
        """
        Generate a graph by initialize nb_nodes, nb_edges and adjacency matrix.

        :param nb_nodes: number of graph nodes.
        :type nb_nodes: int
        :param nb_edges: number of graph edges.
        :type nb_edges: int
        :param edges: graph edges.
        :type edges: list(list(int))
        """
        # test incoherent values
        if nb_nodes < 0 or nb_edges < 0 or len(edges) != nb_edges:
            raise ValueError

        self.__nb_nodes = nb_nodes
        self.__nb_edges = nb_edges
        self.__adj_matrix = [[inf for _ in range(self.__nb_nodes)] for _ in range(self.__nb_nodes)]

        # start node and end node in each edge should have node id between 0 and nb_nodes - 1
        for edge in edges:
            if not (0 <= edge[0] <= self.__nb_nodes - 1 and 0 <= edge[1] <= self.__nb_nodes - 1):
                raise ValueError

            start_node = edge[0]
            end_node = edge[1]
            weight_edge = edge[2]
            self.__adj_matrix[start_node][end_node] = weight_edge

    def get_nb_nodes(self):
        """
        Gets number of graph nodes.

        :return: the number of graph nodes.
        """
        return self.__nb_nodes

    def get_nb_edges(self):
        """
        Gets number of graph edges.

        :return: the number of graph edges.
        """
        return self.__nb_edges

    def get_adj_matrix(self):
        """
        Gets graph adjacency matrix.

        :return: the graph adjacency matrix.
        """
        # we use copy method in order to respect encapsulation.
        new_adj_matrix = [node_neighbors.copy() for node_neighbors in self.__adj_matrix]
        return new_adj_matrix

    def floyd_warshall(self):
        """
        Apply floyd-warshall algorithm on graph.

        :return 
            - dist : dist is a matrix n*n where dist[i][j] represents the shortest distance between i and j.
            - prev : prev is a matrix n*n where prev[i][j] represents the predecessor of j in this shortest path.
        """
        if self.__nb_edges <= 0:
            raise ValueError

        dist, prev = [[0 for _ in range(self.__nb_nodes)] for _ in range(self.__nb_nodes)], [
            [0 for _ in range(self.__nb_nodes)] for _ in range(self.__nb_nodes)]

        # initialization : in this step we set dist and prev by visiting direct paths given by adjacency matrix.
        for i in range(self.__nb_nodes):
            for j in range(self.__nb_nodes):
                dist[i][j] = self.__adj_matrix[i][j]
                prev[i][j] = i

        for i in range(self.__nb_nodes):
            # we set dist[i][i] to 0 because there isn't distance between the node and itself.
            dist[i][i] = 0

        # iterations : in this step we set dist and prev by visiting paths passing through node k.
        for k in range(0, self.__nb_nodes):
            for i in range(0, self.__nb_nodes):
                for j in range(0, self.__nb_nodes):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        # we find a shorter distance between i and j so we actualize it.
                        dist[i][j] = dist[i][k] + dist[k][j]
                        # we also change the predecessor.
                        prev[i][j] = prev[k][j]

        return dist, prev
