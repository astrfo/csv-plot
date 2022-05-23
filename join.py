import os
import pandas as pd
import glob

def create_csv():
    csv_files = glob.glob('*.csv')

    data_list = []
    for file in csv_files:
        name = os.path.splitext(os.path.basename(file))[0]
        data_list.append(pd.read_csv(file, names=[name]))

    df = pd.concat(data_list, axis=1)
    df.to_csv("total.csv",index=False)