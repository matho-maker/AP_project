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

    def get_equipment(self):
        return self.equipment

    def get_weight(self):
        return self.weight

    def get_balance(self):
        return self.balance

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

    # def orientation(self):

    def get_bonus(self):
        return str(self.bonus)

    def __str__(self):
        return "Skier's attributes : " + str(self.dexterity) + ' dexterity, ' + str(
            self.weight) + ' kg, ' + 'equipment: ' + str(self.equipment) + ' ,level: ' + str(
            self.level()) + ' ,balance: ' + str(self.balance)


a = Skiers()
print(a)
b = Skiers()
print(b)

# Create a sample of competitors
Competitors = []
for i in range(10):
  Competitors.append(Skiers())
for n in Competitors:
  print(n)

# Create a dataframe of competitors
Dexterity=[]
for z in Competitors:
  Dexterity.append(z.get_dexterity())

Equipment=[]
for z in Competitors:
  Equipment.append(z.get_equipment())

Weight=[]
for z in Competitors:
  Weight.append(z.get_weight())

Level=[]
for z in Competitors:
  Level.append(z.get_level())

Balance=[]
for z in Competitors:
  Balance.append(z.get_balance())

zipped = list(zip(Dexterity, Equipment, Weight, Level, Balance))
competitors = pd.DataFrame(zipped, columns=('Dexterity','Equipment', 'Weight','Level', 'Balance'))
competitors.index.names = ['Competitor']
print(competitors.head())
