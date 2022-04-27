#####Pygame pre-made map

import numpy as np
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import random
import enum

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
MARGIN = 5

#{'groomed': [0.15,'grey'], 'powder': [0.10,'white'],'ice': [0.6, 'blue'], 'grass':[0.95, 'green'], 'bumps': [0.4, 'grey'], 'trees':1}

def create_map():
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    blue_print = np.random.randint(0, 5, (10, 10))
    grid = []
    for row in range(blue_print.shape[0]):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(blue_print.shape[1]):
            match blue_print[row][column]:
                case 0 :
                    grid[row].append(groomed(row, column))
                case 1 :
                    grid[row].append(powder(row, column))
                case 2 :
                    grid[row].append(ice(row, column))
                case 3 :
                    grid[row].append(grass(row, column))
                case 4 :
                    grid[row].append(bumps(row, column))
                case 5 :
                    grid[row].append(trees(row, column))

    return grid


class cell():
    def __init__(self, row, column): # quand tu ne donnes pas les paramètres toi même ne pas mettre en arguments
        self.row = row
        self.column = column
        self.dimension = 5  # dimension d'une cellule -> 5 x 5 metres, length of the side of a square, a cell = a square
        self.pente = random.randint(6,40) #à vérifier  ---> besoin de la pente ? en %



class constructor(cell):
    def __init__(self, type_construct):
        super().__init__(self,type_construct)
        for typ in self.type:
            self.type_construct = random.choice(typ)  #ou dans cell?

#child class
class groomed(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.15

class powder(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.10

class ice(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.6

class grass(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.95

class bumps(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.4
        #if speed > x: self.fall= 0.8
        #if speed < x: self.fall= 0.2

class trees(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 1
        #if trees: break


grid = create_map()
print(grid)

