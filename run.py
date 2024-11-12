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

#Randomly place the computer's ship
def place_ship():
    row=random.randint(0,GRID_SIZE-1)
    col=random.randint(0,GRID_SIZE-1)
    return row,col


#Main game function
def play_battleships():

    #Create game grid
    grid = create_grid (GRID_SIZE)
    attempts = 0
    
    #Place the computer's ship
    ship_row, ship_col=place_ship()

    # Number of turns for the player
    turns = 2
    print("Let's play Battleships!")
    print("You have", turns, "turns to try and sink the ship by guessing its location on a 5x5 grid.")
    print ("Enter your guesses as row and column numbers (0-4).")
    print_grid(grid)

    #Loop the game
    for turn in range(turns):
        print("\nTurn", turn + 1)
        print_grid(grid)

    #Get player's guess
    try:
        guess_row=int(input("Guess row (0-4):"))
        guess_col=int(input("Guess column (0-4):"))
    except ValueError:
        print("Please enter a valid integer between 0 and 4.")

    #Check if guess is off the grid
    if guess_row <0 or guess_row >=GRID_SIZE or guess_col<0 or guess_col>=GRID_SIZE:
        print ("Try again, that's not on the grid!")




# run the game
play_battleships()