import re


def get_input_info(file_name: str):
    with open(file_name, 'r') as input_info:
        number_of_vertexes, number_of_edges = map(int, re.split(" ", input_info.readline()))
        adjacency_list = [[int(client) for client in re.split(" ", line)] for line in input_info.readlines()][0:number_of_edges+1]

    return adjacency_list
