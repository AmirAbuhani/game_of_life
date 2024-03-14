# This is the second module. This module has the user_living_square function. At the beginning of the game,
# the user choices which cells he is going to populate(this called live cells)
from grid import display_grid


def user_living_square(grid):
    print("You have to enter the address of the cells that you want to populate.")
    # in each iteration, the user populates cell, or he has the option to finish, and the generation process is starting
    while True:
        user_choice = input("A.I want to populate cells\nB.I'm done\n").upper()
        if user_choice == "A":
            row = int(input("Enter the row number: "))
            column = int(input("Enter the column number: "))
            # if the cell has "1" that's mean, the cell is live. otherwise the cell is dead
            grid[row][column] = "1"
        else:
            break

    display_grid(grid)


