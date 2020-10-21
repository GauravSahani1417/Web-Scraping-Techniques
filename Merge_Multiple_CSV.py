import os, glob
import pandas as pd

path = r"C:\Users\gaurav sahani\Desktop\Neubrain Internship\Chief Electorial Office\AC_003 Nandurbar 09-14-19\AC_003_2019\AC_003_19_Excel"

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

merged_df.to_csv(r'C:\Users\gaurav sahani\Desktop\Neubrain Internship\Chief Electorial Office\AC_003 Nandurbar 09-14-19\AC_003_2019\AC_003_19_Excel\AC_003_2019_Merged.csv')