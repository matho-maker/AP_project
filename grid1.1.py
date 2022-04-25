#####Pygame pre-made map


import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

print(grid)