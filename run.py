# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

#Initialize the grid size
GRID_SIZE = 5

#Create a blank grid
def create_grid(size):
    return[["." for _ in range(size)] for _ in range(size)]

