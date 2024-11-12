# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

#Initialize the grid size
GRID_SIZE = 5

#Create a blank grid
def create_grid(size):
    return[["." for _ in range(size)] for _ in range(size)]

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
    

    # Number of turns for the player
    turns=20
    print("Let's play Battleships!")
    print("You have", turns, "turns to try and sink the ship by guessing its location on a 5x5 grid.")
    print ("Enter your guesses as row and column numbers (0-4).")
    print_grid(grid)



# run the game
play_battleships()