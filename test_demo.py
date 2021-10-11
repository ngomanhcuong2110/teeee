import pandas as pd
import numpy as np

df1= pd.read_excel(r'Payoo_Vendor.xlsx','Sheet1',na_values=['NA'])
df2= pd.read_excel(r'Payoo.xlsx','Sheet1',na_values=['NA'])
df1 = df1.set_index('Date ')
df2 = df2.set_index('Date ')

df3 = pd.concat([df1,df2],sort=False)
df3a = df3.stack().groupby(level=[0,1]).unique().unstack(1).copy()


df3a.loc[~df3a.index.isin(df2.index),'status'] = 'notfound' # if not in df2 index then deleted
df3a.loc[~df3a.index.isin(df1.index),'status'] = 'notfound'     # if not in df1 index then new
idx = df3.stack().groupby(level=[0,1]).nunique() # get modified cells. 
df3a.loc[idx.mask(idx <= 1).dropna().index.get_level_values(0),'status'] = 'unmatch'
df3a['status'] = df3a['status'].fillna('match') # assume that anything not fufilled by above rules is the same.
df3a.to_excel("output.xlsx")
print(df3a)