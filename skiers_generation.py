import numpy as np
import math
import random
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Define skier class
class Skiers(object):

    def __init__(self):
        self.dexterity = np.random.randint(60, 100)
        self.equipment = random.choice(['Good', 'Average', 'Bad'])
        self.weight = np.random.randint(50, 100)
        self.balance = np.random.randint(0, 100)
        # self.position =

    def get_dexterity(self):
        return self.dexterity

    def set_dexterity(self, x):
        self.dexterity = x

    def get_equipment(self):
        return self.equipment

    def set_equipment(self, x):
        self.equipment = x

    def get_weight(self):
        return self.weight

    def set_weight(self, x):
        self.weight = x

    def get_balance(self):
        return self.balance

    def set_balance(self, x):
        self.balance = x

    def level(self):

        """This function attribute a level to a skier with respect to its dexterity
        it will enables us to grant bonuses/maluses
        """

        self.level = ' '
        if self.dexterity <= 75:
            self.level = 'Beginner'
        elif self.dexterity > 75 and self.dexterity < 90:
            self.level = 'Average'
        else:
            self.level = 'Pro'
        return self.level

    def get_level(self):
        return self.level

    def set_level(self, x):
        self.level = x

    def bonus(self):

        """Bonus function that gives the skier a time bonus (multiplicator) if according to its level
        - Beginners get an advantage for their risk aversion (as they are more careful they gain time)
        - Average get a malus for their bias confidence
        - Pro get nothing
        """

        self.bonus = ' '
        if self.dexterity <= 75:
            self.bonus = 1.05
        elif self.dexterity > 75 and self.dexterity < 90:
            self.bonus = 0.95
        else:
            self.bonus = 1
        return self.bonus

    def get_bonus(self):
        return str(self.bonus)

    def set_bonus(self, x):
        self.bonus = x

    # def orientation(self):

    def __str__(self):
        return "Skier's attributes : " + str(self.dexterity) + ' dexterity, ' + str(
            self.weight) + ' kg, ' + 'equipment: ' + str(self.equipment) + ' ,level: ' + str(
            self.level()) + ' ,balance: ' + str(self.balance)


a = Skiers()
print(a)
b = Skiers()
print(b)

