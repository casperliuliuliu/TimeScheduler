import pandas as pd

df = pd.read_excel('/Users/liushiwen/Desktop/大四上/gown_app.xlsx')
print(df.columns)
print(df.iloc[6:7])