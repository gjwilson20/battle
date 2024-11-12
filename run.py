# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

#Initialize the grid size
GRID_SIZE = 5

#Create a blank grid
def create_grid(size):
    return[["O" for _ in range(size)] for _ in range(size)]

# Display the grid to the player
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()




#Main game function
def play_battleships():

    #Create game grid
    grid = create_grid (GRID_SIZE)
    attempts = 0

