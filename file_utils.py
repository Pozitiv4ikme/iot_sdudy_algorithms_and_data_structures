import re


# step 1 - read and get input information from file
def get_input_info(file_name: str):
    with open(file_name, "r") as input_info:
        number_of_vertexes, number_of_edges = map(int, re.split(" ", input_info.readline()))
        clients_vertexes = [int(client) for client in re.split(" ", input_info.readline())]
        paths_with_latency = [[int(vertex) for vertex in re.split(" ", line)] for line in input_info.readlines()][
                             0:number_of_edges]
    return number_of_vertexes, number_of_edges, clients_vertexes, paths_with_latency


def put_input_info(file_name: str, info):
    with open(file_name, "w") as output_info:
        output_info.write(str(info))
