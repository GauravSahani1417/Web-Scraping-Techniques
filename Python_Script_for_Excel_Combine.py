import glob
import pandas as pd

path = "C:/Users/gaurav sahani/Desktop/Neubrain Internship/Data Analysis Neubrain"
file_identifier = "*.XLS"

all_data = pd.DataFrame()

for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    
df = pd.DataFrame(all_data)

df.to_csv('Combined_Files_SC.csv')