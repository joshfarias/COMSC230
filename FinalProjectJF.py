'''
Joshua Farias
Profesor Morales
COMSC230
Final Project
2013 French Open Dataset
'''
#imports
import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt

#creates tennis dataframe
tennis = pd.read_csv('https://raw.githubusercontent.com/joshfarias/COMSC230/main/2013-Men-French-Open.csv')

#prints the first portion of dataset
print(tennis.head())

#prints the last portion of dataset
print(tennis.tail())

#First Serve % Player 1 Graph
order = tennis['FSP.1'].value_counts().index
sns.countplot(x="FSP.1", data = tennis, order=order[:25]) #top 25 frequent
plt.xlabel('First Serve [%]')
plt.title('First Serve [%] Frequency for Player1')
plt.show()

#First Serve % Mean Player1
avgP1 = tennis['FSP.1'].mean()
print("Average FSP for Player1:", avgP1)

#First Serve % Player 2 Graph
order = tennis['FSP.2'].value_counts().index
sns.countplot(x="FSP.2", data = tennis, order=order[:25])
plt.xlabel('First Serve [%]')
plt.title('First Serve [%] Frequency for Player2')
plt.show()

#First Serve % Mean Player2
avgP2 = tennis['FSP.2'].mean()
print("Average FSP for Player2:", avgP2)

#Set Results Graph for Player1
sns.countplot(x="FNL.1", data = tennis)
plt.xlabel('Sets')
plt.ylabel('Wins')
plt.title('Sets won by Player 1')
plt.show()

#Set Result Numbers for Player1
print(tennis['FNL.1'].value_counts())

#Set Results for Player2
sns.countplot(x="FNL.2", data = tennis)
plt.xlabel('Sets')
plt.ylabel('Wins')
plt.title('Sets won by Player 2')
plt.show()

#Set Result Numbers for Player2
print(tennis['FNL.2'].value_counts())