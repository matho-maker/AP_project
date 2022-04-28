import random

# Ajouter les coefficients de frictions
class cell():
    def __init__(self, row, column): # quand tu ne donnes pas les paramètres toi même ne pas mettre en arguments
        self.row = row
        self.column = column
        self.dimension = 5  # dimension d'une cellule -> 5 x 5 metres, length of the side of a square, a cell = a square
        self.slope = random.randint(6,40) #à vérifier  ---> besoin de la pente ? en %

#child class of cell by types of land
class groomed(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.15
        self.mu = 0.1

    def get_groomed(self):
        return self.groomed

    def set_groomed(self, x):
        self.groomed = x

    def __repr__(self):
        return "groomed"

class powder(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.10
        self.mu = 0.1
        self.penalty = 1

    def get_powder(self):
        return self.powder

    def set_powder(self, x):
        self.powder = x

    def __repr__(self):
        return "powder"

class ice(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.6
        self.mu = 0.03
        self.penalty = 2

    def get_ice(self):
        return self.ice

    def set_ice(self, x):
        self.ice = x

    def __repr__(self):
        return "ice"

class grass(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.95
        self.mu = 0.2
        self.penalty = 1.5

    def get_grass(self):
        return self.grass

    def set_grass(self, x):
        self.grass = x

    def __repr__(self):
        return "grass"

class bumps(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.4
        #if speed > x: self.fall= 0.8
        #if speed < x: self.fall= 0.2
        self.mu = 0.1
        self.penalty = 1.1

    def get_bumps(self):
        return self.bumps

    def set_bumps(self, x):
        self.bumps = x

    def __repr__(self):
        return "bumps"

class trees(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 1
        #if trees: break
        self.mu = 0
        self.penalty = 9999

    def get_tree(self):
        return self.tree

    def set_tree(self, x):
        self.tree = x

    def __repr__(self):
        return "tree"

class wetsnow(cell):
    def __init__(self, row, column):
        cell.__init__(self, row, column)
        self.fall = 0.5
        self.mu = 0.14
        self.penalty = 1.1

    def get_wetsnow(self):
        return self.wetsnow

    def set_wetsnow(self, x):
        self.ice = x

    def __repr__(self):
        return "wet snow"