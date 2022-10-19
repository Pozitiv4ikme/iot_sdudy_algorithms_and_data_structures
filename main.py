import sys

from dijkstra_algorithm import dijkstra
from file_utils import get_input_info
from graph import Graph
from vertex import Vertex, VertexType


def initialize_graph():
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
            g.clients[vertex.value] = vertex
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

    return g


def minimum_value_of_largest_latency_to_client(graph: Graph):
    """
    using Dijkstra's algorithm, get latency from each router to all vertexes.
    next - find the maximum latency between the router and the all clients.
    if the max latency is minimal, this router can be considered a good position
    for the server.
    :param graph: a Graph object
    """

    # the minimum value of the largest latency to the client at the beginning is equal to infinity (the largest number)
    minimum_value_of_largest_latency_to_client = sys.maxsize

    print('')
    for router in graph.routers:
        # make server vertex
        server = router

        # find latency for all vertexes
        latency_from_start = dijkstra(graph, server)

        # latency from router to router is equal to 0
        longest_router_latency = 0

        for vertex, latency in latency_from_start.items():
            if vertex.v_type is VertexType.CLIENT and latency > longest_router_latency:
                longest_router_latency = latency
        print('End of searching')

        print("Check result of dijkstra's algorithm...\n")
        if longest_router_latency < minimum_value_of_largest_latency_to_client:
            minimum_value_of_largest_latency_to_client = longest_router_latency

    print('Find answer')
    print('The minimum value of the largest latency to client is', minimum_value_of_largest_latency_to_client)


if __name__ == '__main__':
    graph = initialize_graph()
    minimum_value_of_largest_latency_to_client(graph)
