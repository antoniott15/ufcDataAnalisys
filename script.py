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
    fig.suptitle('Average age of fighters')
    return



def init(df):
    averageAge(df)
    plt.show()



def main():
    df = pd.read_csv('./ufcdata/data.csv')
    init(df)


main()