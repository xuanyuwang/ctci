def display(grid, N):
    for row in grid:
        print("\t".join(row))
    print("\n")

def robotInAGrid(N, limits):
    """
    The grid is of size N * N. The upper left cell is (0,0),
    the bottom right cell is (N-1, N-1)
    limits: are cells which the robot cannot step on.
    """
    # symbol is the symbol of each cell. "*" is start cell. "-" is a cell can be reached by going right. "|" is a cell can be reached by going down.
    # path record the path to the current cell.
    # grid record the status and number of possibilities of reaching the current cell. -1 means that it's impossible to reach this cell
    symbol = []
    path = []
    grid = []
    # initialize three matrixes
    for _ in range(N):
        grid.append([0] * N)
        path.append(["*"] * N)
        symbol.append(["*"] * N)
    grid[0][0] = 1
    if len(limits) != 0:
        for i in range(N):
            for j in range(N):
                if (i, j) in limits:
                    grid[i][j] = -1
                    path[i][j] = "@"
                    symbol[i][j] = "@"

    print("initial grid")
    display(symbol, N)

    queue = [(0,0)]

    while grid[N-2][N-1] != -1 or grid[N-1][N-2] != -1:
        if len(queue) == 0:
            return 0
        else:
            cellr, cellc = queue.pop(0)
            if grid[cellr][cellc] == -1:
                continue
            if cellr + 1 < N and cellc < N and grid[cellr+1][cellc] != -1:
                grid[cellr+1][cellc] += grid[cellr][cellc]
                path[cellr+1][cellc] = path[cellr][cellc] + "|"
                symbol[cellr+1][cellc] = "|"
                queue.append((cellr+1, cellc))
            if cellr < N and cellc + 1 < N and grid[cellr][cellc+1] != -1:
                grid[cellr][cellc+1] += grid[cellr][cellc]
                path[cellr][cellc+1] = path[cellr][cellc] + "-"
                symbol[cellr][cellc+1] = "-"
                queue.append((cellr, cellc+1))
            grid[cellr][cellc] = -1
        display(symbol, N)

    return path[N-1][N-1]

if __name__ == "__main__":
    print(robotInAGrid(3, [(1,0)]))
