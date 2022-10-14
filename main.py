import sys

from file_utils import get_input_info
from graph import Graph, dijkstra
from vertex import Vertex, VertexType


def main():
    N, M, clients, paths_with_latency = get_input_info('input.in')

    # step 2.1 - check that we get correct info about number of vertexes and edges
    if not (3 <= N <= 1000 and 2 <= M <= 1000):
        print("You choose bad number of vertexes - must be from 3 to 1000 and edges - from 2 to 1000")
        return

    # step 2.2 - check the number of clients
    for vertex in clients:
        if not (1 <= vertex <= N):
            print(f"You choose bad vertexes who can be clients - must be from 1 to {N}")
            return

    # step 2.3 - check the latency number for all paths
    for path in paths_with_latency:
        if not (1 <= path[2] <= pow(10, 9)):
            print(f"You write bad latency for paths - must be from 1 to {pow(10, 9)}")
            return

    # step 3 - create graph with given number of vertexes and edges
    g = Graph(N, M)

    # step 4 - let's fill graph edges list
    for path in paths_with_latency:
        g.add_edge(path[0], path[1], path[2])

    print("\nEdges in graph:")
    for edge in g.edges:
        print(f"{edge}")

    # step 5.1 - initialize all vertexes
    # and fill graph adjacency list these vertexes for future
    for i in range(1, N + 1):
        # all vertexes from clients list - vertex with type client
        if i in clients:
            vertex = Vertex(i, VertexType.CLIENT)
            g.adjacency_list[vertex] = []
            g.clients.append(vertex)
        # else with type router
        else:
            vertex = Vertex(i, VertexType.ROUTER)
            g.adjacency_list[vertex] = []
            g.routers.append(vertex)

    # step 5.2 - assign all vertices their neighbor/-s
    for vertex, neighbors in g.adjacency_list.items():
        v_i = vertex.value
        for edge in g.edges:
            if edge.from_v == v_i and edge not in g.adjacency_list[vertex]:
                g.adjacency_list[vertex].append(edge)

    print("\nVisualize graph by adjacency list:")
    for vertex, neighbour in g.adjacency_list.items():
        print(f"{vertex} has neighbour/-s {neighbour}")


if __name__ == '__main__':
    main()
