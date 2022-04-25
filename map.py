#####Pygame pre-made map


import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

print(grid)

""" Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------                 ###probably not needed
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        else:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid                                      ###visualization
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()


class cell():
    def __init__(self, row, column, type, dimension, pente, pass_on):
        self.row = row
        self.column = column
        self.type = {'groomed': [0.15,'gray'], 'powder': [0.10,'white'],'ice': [0.6, 'blue'], 'grass':[0.95, 'green'], 'bumps': [0.4, 'grey'], 'trees':1} #bumps si va vite tombe sinon tombe pas,
        self.dimension_cell = 5  # dimension d'une cellule -> 5 x 5 metres, length of the side of a square, a cell = a square
        self.pente = random.randint(6,40) #à vérifier  ---> besoin de la pente ? en %
        self.pass_on = [0,1]

#classe fille pour chaque type

class groomed(cell):
    def __


class constructor(cell):
    def __init__(self, type_construct):
        super().__init__(self,type_construct)
        for typ in self.type:
            self.type_construct = random.choice(typ)  #ou dans cell?

#    def neighbor(self):
 #       for j in column:
  #          if (self.type_construct=='tree' and grid[i][j]):
   #             while self.type_construct == random.choice(type)

##à compléter




   # def new_cell(self, grid, i, j):  # row=i, column=j
    #    for i in row:  ##still needed?
     #       for j in column:
      #          grid[i][j] = new_cell()  #  -> grid car veut ajouter des nouveaux types de cellules

    def pass_on_cell(self, pass_on):  # event type = 1 if pass on cell, =0 if can't pass on cell
        if pass_on == 1:
            return pygame.event.set_allowed.pass_on_cell()
        elif pass_on == 0:
            return pygame.event.set_blocked.pass_on_cell()
        if self.type_construct== 'tree':
            pass_on ==0


#color for the map
def random_color(search=None):
    get a single random Color(), with Optional search filter.
        search='green' will return 'seagreen', 'bluegreen', etc...

    default to choice() of full list
    if search:
        c = random.choice(search_color(search))
    else:
        c = random.choice(THECOLORS.values())

    # debug: print type(c), c # returns Color()
    return c
    # todo: exception on color search fail? OR just default to white.


def search_color(name):
    search pygame. THECOLORS for a name, example:
        "green" -> seagreen, bluegreen, darkgreen
    
    # verbose:    print "search_color( {} ) =".format(name)
    return [Color(c) for c in pygame.color.THECOLORS if name in c]

# for search*
color_groups = ['', 'white', 'purple', 'green', 'dark', 'light', 'red', 'blue', 'orange', 'gray', 'blue', 'green']

'''class neighbor():
    def __init__(self):

    def
        # class neighbor chaque cell a une liste de ces voisins, (inclure dedans contrainte tree? mieux maybe?)
        #va vers l'extérieur

        # faire un autre def?
        for i in row:
            if cell(type_construct == "trees")[i] and cell(type_construct == "trees")[i + 1]:  # ne pas avoir ligne d'arbres    ##appeler les coord de la grille?
                type_construct[i] = random.choice(
                    type)  # reroll the random choice of one or multiple cell in the row in order to avoid a full line of trees
                # ou .droplevel() une case, une ligne
'''
##def viz_map():                                                            # fonction audrey pour la visualisation
# viz= np.zeros[nb_lines,nb_col]
# for i in nb_lines:
#  for j in nb_column:
#    viz[i][j]= map[i][j].type.to_string()
# print(viz)


##Notes: pygame.event: https://www.pygame.org/docs/ref/event.html
# pygame.event.get_grab: test if the program is sharing input devices, for skiers?
# pygame.sprite: https://www.pygame.org/docs/ref/sprite.html
#grid autre: https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame

#qui va vers l'extérieur, proba de type de terrain change si bcp de glace à une endroit plus -> rapport entre


'''-voir .clock
-voir neighbor pour jolie carte colorée -> un type = une couleur
-voir neighbor avec pas ligne case de tree'''
"""