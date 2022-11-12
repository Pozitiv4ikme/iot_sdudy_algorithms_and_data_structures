import sys

from dijkstra_algorithm import dijkstra
from file_utils import get_input_info, put_input_info
from graph import Graph
from vertex import Vertex, VertexType


def initialize_graph() -> Graph | None:
    """
    initialize and fill Graph by read info from input file

    The input file gamsrv.in consists of M + 2 lines.
        • The first line contains N and M — the number of nodes and connections, respectively.
            3 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
        • The second line contains a list of integers separated by a space — numbers
            nodes that are clients. All nodes in the network are numbered from 1 to N.
        • The next M lines contain triplets of natural numbers startnode, endnode, latency
            — the number of the start node, the end node and the delay for each connection.
            1 ≤ latency ≤ 109
    :return g: the Graph or None
    """

    N, M, clients, paths_with_latency = get_input_info('gamsrv.in')

    # step 2.1 - check that we get correct info about number of vertices and edges
    if not (3 <= N <= 1000 and 2 <= M <= 1000):
        print("You choose bad number of vertices - must be from 3 to 1000 and edges - from 2 to 1000")
        return

    # step 2.2 - check the number of clients
    for vertex in clients:
        if not (1 <= vertex <= N):
            print(f"You choose bad vertices who can be clients - must be from 1 to {N}")
            return

    # step 2.3 - check the latency number for all paths
    for path in paths_with_latency:
        if not (1 <= path[2] <= pow(10, 9)):
            print(f"You write bad latency for paths - must be from 1 to {pow(10, 9)}")
            return

    # step 3 - create graph with given number of vertices and edges
    g = Graph(N, M)

    # step 4 - let's fill graph edges list
    for path in paths_with_latency:
        g.add_edge(path[0], path[1], path[2])

    print("\nEdges in graph:")
    for edge in g.edges:
        print(f"{edge}")

    # step 5.1 - initialize all vertices
    # and fill graph adjacency list these vertices for future
    for i in range(1, N + 1):
        if i in clients:
            vertex = Vertex(i, VertexType.CLIENT)
            g.adjacency_list[vertex] = []
            g.clients[vertex.value] = vertex
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


def minimum_value_of_largest_latency_to_client(graph: Graph) -> int:
    """
    using Dijkstra's algorithm, get latency from each router to all clients.
    find the maximum latency between the router and the all clients.
    if the max latency is minimal, this router can be considered a good position for the server.
    :param graph: a Graph object
    :return minimum_value: the minimum value of the largest latency to client
    """

    minimum_value = sys.maxsize

    for router in graph.routers:
        # make server vertex
        server = router

        # find latency for all vertices
        latency_from_start = dijkstra(graph, server)

        # latency from router to router is equal to 0
        longest_server_latency = 0

        # find the largest path latency among all vertices in dict latency from start
        for vertex, latency in latency_from_start.items():
            if vertex.v_type is VertexType.CLIENT and latency > longest_server_latency:
                longest_server_latency = latency

        # finding the smallest among the largest
        if longest_server_latency < minimum_value:
            minimum_value = longest_server_latency

    print('\nThe minimum value of the largest latency to client is', minimum_value)

    return minimum_value


if __name__ == '__main__':
    graph = initialize_graph()
    result = minimum_value_of_largest_latency_to_client(graph)
    put_input_info('gamsrv.out', result)
