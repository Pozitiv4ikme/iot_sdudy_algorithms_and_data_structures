from collections import defaultdict
from queue import LifoQueue


class Graph:
    def __init__(self):
        # Use defaultdict because this is error free way to use
        # any key without initialization of its value,
        # it has to be told the type of default container of all its keys.
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def represent_graph(self):
        print("vertex" + (2 * " ") + "neighbours")
        for vertex, neighbours in self.graph.items():
            print(f"{vertex}" + (6 * " ") + f"{neighbours}")

    def check_neighbours(self):
        print(self.graph[3])

    def dfs(self, vertex):
        visited = defaultdict(bool)

        for v in self.graph:
            visited[v] = False

        stack = LifoQueue()

        stack.put(vertex)

        result = ""

        while not stack.empty():
            vertex = stack.get()

            if not visited[vertex]:
                visited[vertex] = True

                result = result + str(vertex) + " "

                for neighbours in self.graph[vertex]:
                    if not visited[neighbours]:
                        stack.put(neighbours)

        print(result)

    def get_vertex(self):
        vertexes = []
        for vertex, neighbours in self.graph.items():
            vertexes.append(vertex)
        return vertexes

    def __str__(self):
        return f"graph - {self.graph.items()}"
