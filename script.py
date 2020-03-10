import pandas as pd
import collections
import matplotlib.pyplot as plt
import numpy as np

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
    loser = []
    winer = []
    df = df.dropna(how='all')
    for _, values in df.iterrows():
        if(values['Winner'] == 'Red'):
            winer.append(values['R_fighter'])
            loser.append(values['B_fighter'])
        elif ( values['Winner'] == 'Blue'):
            loser.append(values['R_fighter'])
            winer.append(values['B_fighter'])
    lose = dict(collections.Counter(loser))
    win = dict(collections.Counter(winer))
    fighter = {}
    for elements in lose:
        if elements in lose and elements in win:
            if win[elements]-lose[elements] < 0:
                fighter[elements] = {'lose': lose[elements], 'wins': win[elements], 'total':win[elements]-lose[elements]}
    c = {k: v for k, v in sorted(fighter.items(), key=lambda item: item[1]['total'])[:11]}
    names = []
    wins = []
    loses = []
    width = 0.25
    for elements in c:
        names.append(elements)
        wins.append(c[elements]['wins'])
        loses.append(c[elements]['lose'])
    labelslen = np.arange(len(names))
    fig, ax = plt.subplots()
    rects1 = ax.bar(labelslen - width/2, wins, width, label='Wins')
    rects2 = ax.bar(labelslen + width/2, loses, width, label='Loses')
    ax.set_ylabel('Quantity')
    ax.set_title('Wins and Loses by a fighter')
    ax.set_xticks(labelslen)
    ax.set_xticklabels(names)
    ax.tick_params(axis='x', rotation=70)
    ax.legend()
    autolabel(rects1,ax)
    autolabel(rects2,ax)
    plt.savefig(PATH + 'losest.png',bbox_inches='tight')


def autolabel(rects,ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')



def init(df):
    df = df.dropna(axis='rows')
    averageAge(df)
    mostOldMostWins(df)
    worstFighter(df)



def main():
    df = pd.read_csv('./ufcdata/data.csv')
    init(df)


main()