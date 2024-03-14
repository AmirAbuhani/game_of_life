Author: Amir Abu Hani

Game of Life project is simulating the Conway's Game of Life. It is consists from 5 modules:

The first module is grid, which display the grid for each step in the game. the grid will be shown in the beginning, 
after the user populated cells and in each generation.

The second module is the user_inputs, which allowing the user to populate many cells that he wants in the grid. 
populate cells are alive cells with '1' in it.

The third module is game_logic, which contains how generation well be according to specific rules.
Here are the game rules:

1- if alive cell has at less than 2 live neighbors, this cell is becoming dead in the next generation.

2- if alive cell has 2 or 3 live neighbors, this cell is remaining alive in the next generation. 

3- if alive cell has more than 3 live neighbors, this cell is becoming dead in the next generation.

4- if dead cell has exactly 3 live neighbors, this cell becoming live in the next generation.

The fourth module is simulator, which simulates the game according to the rounds number. after each
generation, the result will be shown to the user.

The final module is simulator_in_cli. this is the interface that the game will be run in it. 
