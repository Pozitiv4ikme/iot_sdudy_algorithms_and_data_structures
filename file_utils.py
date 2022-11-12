import re


# step 1 - read and get input information from file
def get_input_info(file_name: str) -> tuple[int, int, list[int], list[list[int]]]:
    """
    read input info from given file for given Graph
    :param file_name: file with input info
    :returns tuple with:
        - number of vertices;
        - number of edges;
        - list of clients vertices;
        - list of paths from one Vertex to another with latency
    """
    with open(file_name, "r") as input_info:
        number_of_vertices, number_of_edges = map(int, re.split(" ", input_info.readline()))
        clients_vertices = [int(client) for client in re.split(" ", input_info.readline())]
        paths_with_latency = [[int(vertex) for vertex in re.split(" ", line)] for line in input_info.readlines()][
                             0:number_of_edges]
    return number_of_vertices, number_of_edges, clients_vertices, paths_with_latency


def put_input_info(file_name: str, info) -> None:
    """
    write output info into given file
    :param file_name: given file name
    :param info: info to write into file
    :return None:
    """
    with open(file_name, "w") as output_info:
        output_info.write(str(info))
