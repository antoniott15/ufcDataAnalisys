import csv
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

PATH = './plots/'

#
# Gets x: age y:quantity, all ages of the fighters
#
def averageAge(df):
    c = collections.Counter(df['R_age'])
    height = []
    repetitions = []
    for values in c.items():
        height.append(values[0])
        repetitions.append(values[1])

    fig, axes =  plt.subplots()
    axes.bar(height,repetitions)
    fig.suptitle('Age of Fighters')
    plt.savefig(PATH + 'ageOfFigthers.png')
    return


#
# Get age through name
#
def getYearByName(df,name):
    for _, values in df.iterrows():
        if values['R_fighter'] == name:
            return values['R_age']
        if values['B_fighter'] == name:
            return values['B_age']

#
#  Scale between the 10 most winners by age
#           
def mostOldMostWins(df):
    winner = []
    ageOfFighter = {}
    for _,values in df.iterrows():
        ageOfFighter[values['R_fighter']] = values['R_age']
        if(values['Winner'] == 'Red'):
            winner.append(values['R_fighter'])
        elif ( values['Winner'] == 'Blue'):
            winner.append(values['B_fighter'])
    c = dict(collections.Counter(winner).most_common(10))
    fighter = {}
    for elements in c:
        fighter[elements] = {'age': ageOfFighter[elements],'wins':c[elements]}
    fighterTitle = []
    value = []
    for elements in fighter:
        fighterTitle.append(elements[0:12] + " "+ str(fighter[elements]['age']))
        value.append(fighter[elements]['wins'])
    fig, ax = plt.subplots()
    ax.scatter(value,fighterTitle)
    plt.savefig(PATH + 'mostOld.png',bbox_inches='tight')
    return


#
# The fighter that has more loses than wins by far
#    
def worstFighter(df):
    

def init(df):
    df = df.dropna(axis='rows')
    averageAge(df)
    mostOldMostWins(df)
    worstFighter(df)



def main():
    df = pd.read_csv('./ufcdata/data.csv')
    init(df)


main()