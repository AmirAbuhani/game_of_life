# This the third module. this module contains the game_of_life_rules function.
# As we know, Conway's Game of Life has 4 rules:
# 1- if alive cell has at less than 2 live neighbors, this cell is becoming dead in the next generation
# 2- if alive cell has 2 or 3 live neighbors, this cell is remaining alive in the next generation
# 3- if alive cell has more than 3 live neighbors, this cell is becoming dead in the next generation
# 4- if dead cell has exactly 3 live neighbors, this cell becoming live in the next generation
from grid import display_grid


def game_of_life_rules(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[" " for _ in range(cols)] for _ in range(rows)]  # Create a new grid to store the next generation
    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0
            # to ensure the only accessing valid indices within the boundaries of the grid
            # in this step, we "create" small matrix each iteration
            # for each cell, we check his neighbors(up, down and diagonal) if are alive("1")
            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    # if the cell is live and not the current cell, we are adding the live_neighbors variable by 1
                    if (x, y) != (i, j) and grid[x][y] == "1":
                        live_neighbors += 1

            # Apply rules(at the beginning of the file)
            if grid[i][j] == "1":
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = " "  # Cell dies
                else:
                    new_grid[i][j] = "1"  # Cell remains alive
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = "1"  # Cell becomes alive

    # Update the original grid with the next generation
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = new_grid[i][j]

    display_grid(grid)  # Assuming create_grid is defined elsewhere


