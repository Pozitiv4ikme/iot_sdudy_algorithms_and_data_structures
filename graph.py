from edge import Edge


class Graph:
    def __init__(self, num_of_vertices: int, num_of_edges: int):
        self.v = num_of_vertices
        self.e = num_of_edges
        self.edges = []
        self.adjacency_list = {}
        self.clients = {}
        self.routers = []

    def add_edge(self, start, end, weight) -> None:
        self.edges.append(Edge(start, end, weight))
        self.edges.append(Edge(end, start, weight))
