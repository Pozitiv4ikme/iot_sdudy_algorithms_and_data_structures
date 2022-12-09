import sys

from graph import Graph
from vertex import Vertex, VertexType

MAX_INT = sys.maxsize


# make func with two arguments - graph and start vertex(node)
def dijkstra(graph: Graph, start_point: Vertex) -> dict:
    """
    implement Dijkstra's algorithm
    :param graph: Graph for which we will apply Dijkstra's algorithm
    :param start_point: start Vertex for our algorithm
    :return distances_from_start: a dictionary with all vertices and their shortest path latency values
    """
    # create some list to check that we visit this vertex or no
    unvisited_vertices = graph.adjacency_list.copy()

    # create list to record the path latency to the vertex from the starting point
    # set 0 for start point and infinity ( represents by the largest value a system can store ) for other vertices
    distances_from_start = {
        vertex: (0 if vertex == start_point else MAX_INT) for vertex in graph.adjacency_list.keys()
    }

    # found the shortest way from start to all others vertex
    while unvisited_vertices:
        # from unvisited vertices - choose the one with the shortest path
        # by min() with param key (unvisited_vertices return vertex,
        # pass this vertex like param for lambda,
        # take value by key from dictionary distance from start,
        # make comparisons by this value and find min)
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances_from_start[vertex])

        # since we visited it, we will note this
        # by deletes it from unvisited vertices list
        del unvisited_vertices[current_vertex]

        # now we check neighbour/-s of current vertex and make relaxation ( update latency for all vertices )
        for edge in graph.adjacency_list[current_vertex]:
            # take info from edge about vertex and create it
            neighbour = Vertex(edge.to_v, VertexType.CLIENT if (edge.to_v in graph.clients) else VertexType.ROUTER)

            if neighbour in unvisited_vertices:
                # take value of latency for this edge
                latency = edge.e_weight

                # update latency for current vertex in dict
                update_latency = distances_from_start[current_vertex] + latency

                # check whether the new value is less than the previous one
                if update_latency < distances_from_start[neighbour]:
                    distances_from_start[neighbour] = update_latency
            else:
                continue

            # print(distances_from_start) - represent every step in algorithm

    return distances_from_start
