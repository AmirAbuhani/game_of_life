# This is the first module
# In this module, there is a display_grid function that display the grid in each step during the game
# for example, when the game is starts or when the user choices the populated cells or in all the generations
def display_grid(grid):
    for i in range(8):
        print("|", end="")
        for j in range(8):
            print("___|", end="")
        print()

        print("|", end="")
        for j in range(8):
            print(" {} |".format(grid[i][j]), end="")
        print()

    print("|", end="")
    for j in range(8):
        print("___|", end="")
    print()



