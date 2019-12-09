import csv
import pandas as pd
import numpy as np



def init(row):
    df = pd.DataFrame(row)
    des = df.describe()
    des.replace(np.nan,"0")
    print(des)


def main():
    with open('./ufcdata/data.csv', newline='') as File:  
        reader = csv.reader(File)
        rows = []
        for row in reader:
            rows.append(row)
        init(rows)


main()