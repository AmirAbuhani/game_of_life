# This is the fourth module. this will be the simulator(run game)
# we can use this module for different interfaces without modifying the game logic
from grid import display_grid
from game_logic import game_of_life_rules
from user_inputs import user_living_square


# This function determines the game steps.
# The function has the grid size and the number of the simulation rounds
def run_game(size, rounds):
    # At first, the grid is empty(all the cells is dead)
    grid = [[" " for _ in range(size)] for _ in range(size)]
    display_grid(grid)
    # the user decided which cells is alive("1")
    user_living_square(grid)
    print()

    rounds_number = rounds
    round_index = 1
    # simulate according to the rounds number
    while rounds_number > 0:
        print(f"Round {round_index} results: ")
        game_of_life_rules(grid)
        print()
        round_index += 1
        rounds_number -= 1
