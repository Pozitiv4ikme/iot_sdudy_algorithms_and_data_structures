import re
from FloodFill import bfs

if __name__ == '__main__':

    # read from input.txt file
    with open("input.txt", "r") as input_info:
        field_height, field_width = map(int, re.split(",", input_info.readline()))
        x_pos, y_pos = map(int, re.split(",", input_info.readline()))
        replacement_color = input_info.readline().strip("'\n")
        input_matrix = [[str(color) for color in re.findall('\w+', line)] for line in
                        input_info.readlines()[3:field_width + 3]]

    bfs(field_height, field_width, x_pos, y_pos, replacement_color, input_matrix)

    # write into output.txt file
    with open("output.txt", "w") as result:
        for row in input_matrix:
            print(row)
            result.write(f'{row}\n')
