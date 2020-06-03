
import pandas as pd
from pandas_profiling import ProfileReport


df=pd.read_csv('Sales By Geography.csv')
print(df)



#generate a report

profile=ProfileReport(df)
profile.to_file(output_file="Sales By Geography.html")

