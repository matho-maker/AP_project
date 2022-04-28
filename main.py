# -----------------------------------------------------------
# Advanced Programming
# Mathilde BOCCARA - Piotr Kolecki
# Géraldine RAIDY
# UniL - MscF - Spring 2022
# ---------------------------------------------------------


import numpy as np
import math
import pandas as pd
from skiers_generation import Skiers

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



if __name__ == "__main__":
    main()
