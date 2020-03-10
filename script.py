import csv
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

PATH = './plots/'


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


def getYearByName(df,name):
    for _, values in df.iterrows():
        if values['R_fighter'] == name:
            return values['R_age']
        if values['B_fighter'] == name:
            return values['B_age']
            

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
    x = {k: v for k, v in sorted(ageOfFighter.items(), key=lambda item: item[1], reverse=True)}
    fighter = {}
    for elements in c:
        fighter[elements] = {'age': x[elements],'wins':c[elements]}
    fighterTitle = []
    value = []
    for elements in fighter:
        fighterTitle.append(elements[0:12] + " "+ str(fighter[elements]['age']))
        value.append(fighter[elements]['wins'])
    fig, ax = plt.subplots()
    ax.scatter(value,fighterTitle)
    plt.savefig(PATH + 'mostOld.png')
    return


            
    


def init(df):
    df = df.dropna(axis='rows')
    averageAge(df)
    mostOldMostWins(df)
  



def main():
    df = pd.read_csv('./ufcdata/data.csv')
    init(df)


main()