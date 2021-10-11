 #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
import csv
import pandas as pd
# read flash.dat to a list of lists
with open('D:\\Project\\credit\\091421_ISS_DOB_970406_1_TC_SWC.dat', 'r') as fin:
    data = fin.read().splitlines(True)

data_new=data[1:-1]
data_new1=[]
label=(" ","[MTI]","[F2]","[F3]","[SVC]","[TCC]","[F4]","[RTA]","[F49]","[F5]","[F50]","[F9]","[F6]","[RCA]","[F51]","[F10]","[F11]","[F12]","[F13]","[F15]","[F18]","[F22]","[F25]","[F41]","[ACQ]","[ISS]","[MID]","[BNB]","[F102]" ,"[F103]","[SVFISSNP]","[IRFISSACQ]","[IRFISSBNB]","[SVFACQNP]","[IRFACQISS]","[IRFACQBNB]","[SVFBNBNP]","[IRFBNBISS]","[IRFBNBACQ]","[F37]","[F38]","[TRN]","[RRC]","[RSV1]", "[RSV2]","[RSV3]","[CSR]")

for i in range(0,len(data_new)):
    d=[]
    dat=data_new[i].split("]")
    for da in dat:
        d1=da.split("[")        
        d.append(d1[0])
    data_new1.append(d)
tab=pd.DataFrame(data_new1,columns=label)
print(tab)
tab.to_excel("output1.xlsx")
df1=tab
df2=tab
df1 = df1.set_index('[F15]')
df2 = df2.set_index('[F15]')

df3 = pd.concat([df1,df2],sort=False)
df3a = df3.stack().groupby(level=[0,1]).unique().unstack(1).copy()


df3a.loc[~df3a.index.isin(df2.index),'status'] = 'notfound' # if not in df2 index then deleted
df3a.loc[~df3a.index.isin(df1.index),'status'] = 'notfound'     # if not in df1 index then new
idx = df3.stack().groupby(level=[0,1]).nunique() # get modified cells. 
df3a.loc[idx.mask(idx <= 1).dropna().index.get_level_values(0),'status'] = 'unmatch'
df3a['status'] = df3a['status'].fillna('match') # assume that anything not fufilled by above rules is the same.
df3a.to_excel("output.xlsx")
print("df3: ",df3)