from file_utils import get_input_info
from graph import Graph

if __name__ == '__main__':
    adjacency_list = get_input_info('input.txt')

    g = Graph()
    for path in adjacency_list:
        g.addEdge(path[0], path[1])

    g.represent_graph()

    print()
    g.dfs(0)
