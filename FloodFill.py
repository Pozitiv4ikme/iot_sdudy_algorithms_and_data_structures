from queue import Queue


def bfs(h: int, w: int, x: int, y: int, r_color: str, matrix):
    # 1 step - find old color by x and y coordinate
    old_color = matrix[max(0, x - 1)][max(0, y - 1)]

    # 2 step - create queue
    q = Queue()

    # 3 step - create matrix and mark all the V as not visited
    visited = [[False for x in range(h)] for y in range(w)]

    # 4 step - append in queue start V ( his x and y coordinate )
    q.put([max(0, x - 1), max(0, y - 1)])

    # 5 step - start find all V with same color
    while not q.empty():
        # Dequeue current V
        x, y = q.get()

        # check whether this V has the desired color
        if matrix[x][y] != old_color:
            # skip this cases
            continue

        # cases when found current V neighbours
        else:
            visited[x][y] = True

            matrix[x][y] = r_color

            # cases on x - bottom, top current V neighbours
            if 0 <= x and x + 1 <= w - 1:
                if not visited[x + 1][y]:
                    q.put((x + 1, y))

            if x >= 0 and x - 1 >= 0:
                if not visited[x - 1][y]:
                    q.put((x - 1, y))

            # and y - right, left current V neighbours
            if 0 <= y and y + 1 <= h - 1:
                if not visited[x][y + 1]:
                    q.put((x, y + 1))

            if y >= 0 and y - 1 >= 0:
                if not visited[x][y - 1]:
                    q.put((x, y - 1))
