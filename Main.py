import re
from FloodFill import bfs

if __name__ == '__main__':

    # read from input.txt file
    with open("input.txt", "r") as input_info:
        field_param = re.split(",", input_info.readline().strip())
        field_height: int = int(field_param[0])
        field_width: int = int(field_param[1])

        pos_param = re.split(",", input_info.readline())
        x_pos: int = int(pos_param[0])
        y_pos: int = int(pos_param[1])

        replacement_color = input_info.readline().strip("'\n")

        input_matrix = [[str(color) for color in re.findall('[A-Z]', line)] for line in input_info.readlines()][
                       0:field_width]

    bfs(field_height, field_width, x_pos, y_pos, replacement_color, input_matrix)

    # write into output.txt file
    with open("output.txt", "w") as result:
        for row in input_matrix:
            print(row)
            result.write(f'{row}\n')
