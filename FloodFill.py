from queue import Queue


def bfs(h: int, w: int, x: int, y: int, r_color: str, matrix):

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

    # 4 step - create queue
    q = Queue()

    # 5 step - append in queue needed V ( his x and y coordinate )
    q.put([x, y])

    # 6 step - start find all V with same color
    while not q.empty():
        # Dequeue current V and take his neighbors on x and y line
        x, y = q.get()

        # check bounds of field and their color
        if x < 0 or x >= w or y < 0 or y >= h or matrix[x][y] != old_color:
            # skip this cases
            continue

        # cases when found required V
        else:
            matrix[x][y] = r_color

            # cases on x - top, bottom
            q.put((x + 1, y))
            q.put((x - 1, y))

            # and y - top, bottom V
            q.put((x, y + 1))
            q.put((x, y - 1))
