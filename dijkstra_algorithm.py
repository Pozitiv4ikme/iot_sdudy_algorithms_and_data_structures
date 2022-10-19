import sys

from graph import Graph
from vertex import Vertex, VertexType

MAX_INT = sys.maxsize


# make func with two arguments - graph and start vertex(node)
def dijkstra(graph: Graph, start_point: Vertex):
    # create some list to check that we visit this vertex or no
    unvisited_vertexes = graph.adjacency_list.copy()

    # create list to record the path to the vertex from the starting point
    # set 0 for start point and infinity ( represents by the largest value a system can store ) for other vertices
    distances_from_start = {
        vertex: (0 if vertex == start_point else MAX_INT) for vertex in graph.adjacency_list.keys()
    }

    # found the shortest way from start to all others vertex
    while unvisited_vertexes:
        # from unvisited vertexes - choose the one with the shortest path
        # by min() with param key where we pass iterator and make comparison
        current_vertex = min(unvisited_vertexes, key=lambda vertex: distances_from_start[vertex])

        # since we visited it, we will note this
        # by deletes it from unvisited vertexes list
        del unvisited_vertexes[current_vertex]

        # now we check neighbour/-s of current vertex and make relaxation ( update latency for all vertexes )
        for edge in graph.adjacency_list[current_vertex]:
            # take info from edge about vertex and create it
            neighbour = Vertex(edge.to_v, VertexType.CLIENT if (edge.to_v in graph.clients) else VertexType.ROUTER)

            # take previous value of latency for this edge
            latency = edge.e_weight

            # update latency for current vertex
            update_latency = distances_from_start[current_vertex] + latency

            # check whether the new value is less than the previous one
            print(distances_from_start)
            if update_latency < distances_from_start[neighbour]:
                distances_from_start[neighbour] = update_latency

    return distances_from_start
