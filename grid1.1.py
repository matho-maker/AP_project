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
        grid[row].append('cell')  # Append a cell

class cell():
    def __init__(self, row, column, type, dimension, pente):
        self.row = row
        self.column = column
        self.type = {'groomed': [0.15,'grey'], 'powder': [0.10,'white'],'ice': [0.6, 'blue'], 'grass':[0.95, 'green'], 'bumps': [0.4, 'grey'], 'trees':1} #bumps si va vite tombe sinon tombe pas,
        self.dimension_cell = 5  # dimension d'une cellule -> 5 x 5 metres, length of the side of a square, a cell = a square
        self.pente = random.randint(6,40) #à vérifier  ---> besoin de la pente ? en %

    def get_type(self):
        return(self.type)


class constructor(cell):
    def __init__(self, type_construct):
        super().__init__(self,type_construct)
        for typ in self.type:
            self.type_construct = random.choice(typ)  #ou dans cell?

#child class
class groomed(cell):
    def __init__(self, row, column, type, dimension, pente):
        cell.__init__(self, row, column, type, dimension, pente)
        self.fall = 0.15
class powder(cell):
    def __init__(self, row, column, type, dimension, pente):
        cell.__init__(self, row, column, type, dimension, pente)
        self.fall = 0.10
class ice(cell):
    def __init__(self, row, column, type, dimension, pente):
        cell.__init__(self, row, column, type, dimension, pente)
        self.fall = 0.6
class grass(cell):
    def __init__(self, row, column, type, dimension, pente):
        cell.__init__(self, row, column, type, dimension, pente)
        self.fall = 0.95
class bumps(cell):
    def __init__(self, row, column, type, dimension, pente):
        cell.__init__(self, row, column, type, dimension, pente)
        self.fall = 0.4
        #if speed > x: self.fall= 0.8
        #if speed < x: self.fall= 0.2
class trees(cell):
    def __init__(self, row, column, type, dimension, pente):
        cell.__init__(self, row, column, type, dimension, pente)
        self.fall = 1
        #if trees: break



print(grid)

