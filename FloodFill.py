from collections import deque


def bfs(h: int, w: int, x: int, y: int, r_color: str, matrix: list[list[str]]):

    # 1 step - check if matrix exist
    if not matrix:
        print("You need to have input matrix!")
        return

    # 2 step - find old color by x and y coordinate
    old_color = matrix[x][y]

    # 3 step - check if old color no same with new
    if r_color == old_color:
        print("You pass the same color to change")
        return

    # 3 step - create queue
    q = deque()

    # 4 step - append in queue start V
    q.append(matrix[x][y])

    # 5 step - start find all V with same color
    while len(q) > 0:
        # pop current V
        q.pop()

        # take his neighbors on x and y line

        # check bounds of field and their color

        # if the same - make new color


