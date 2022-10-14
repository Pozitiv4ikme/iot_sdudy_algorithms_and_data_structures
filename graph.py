import sys
from edge import Edge
from vertex import Vertex, VertexType


class Graph:
    def __init__(self, num_of_vertices: int, num_of_edges: int):
        self.v = num_of_vertices
        self.e = num_of_edges
        self.edges = []
        self.adjacency_list = {}
        self.unvisited = []
        self.clients = []
        self.routers = []

    def add_edge(self, start, end, weight) -> None:
        self.edges.append(Edge(start, end, weight))
        self.edges.append(Edge(end, start, weight))


def dijkstra(graph: Graph, start_point: Vertex):
    # make all vertex unvisited
    # for vertex in graph.adjacency_list.keys():
    #     graph.unvisited.append(vertex)

    unvisited_vertices = graph.adjacency_list.copy()

    distances_from_start = {
        vertex: (0 if vertex == start_point else sys.maxsize) for vertex in graph.adjacency_list.keys()
    }

