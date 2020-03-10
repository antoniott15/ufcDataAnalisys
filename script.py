import csv
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

# Counter of Red corder
#      ages
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
    return


def mostOldMostWins(df):
    df = df.sort_values(by=['B_age', 'R_age'],ascending=False)
    winner = []
    for _,values in df.iterrows():
        if(values['Winner'] == 'Red'):
            winner.append(values['R_fighter'])
        elif ( values['Winner'] == 'Blue'):
            winner.append(values['B_fighter'])
    c = collections.Counter(winner).most_common(10)
    print(c)
    


def init(df):
    df = df.dropna(axis='rows')
    #averageAge(df)
    mostOldMostWins(df)
    #plt.show()



def main():
    df = pd.read_csv('./ufcdata/data.csv')
    init(df)


main()