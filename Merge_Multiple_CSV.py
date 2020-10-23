import os, glob
import pandas as pd

path = r"Path where the excel files are stored"

all_files = glob.glob(os.path.join(path, "AC_*_*_*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',', header=None)
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_df = pd.concat(all_df)

merged_df.drop('file', axis='columns', inplace=True)

merged_df['Year'] = 2019
merged_df['Election_Type'] = "Assembly"

merged_df.to_csv('path to store the csv file')
