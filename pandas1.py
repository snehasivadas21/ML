import pandas as pd
import numpy as np

# s=pd.Series()
# print(s)

# data=np.array(['s','n','e','h','a'])
# s=pd.Series(data)
# r=pd.Series(data,index=[11,22,33,44,55])
# print(s)
# print(s[:2])
# print(r[33])

# d={"a":10,"b":20,"c":30}
# ds=pd.Series(d)
# print(ds)

# r=pd.Series(range(5,15))
# print(r)

# l=pd.Series(range(1,20,3),index=[x for x in 'abcdefg'])
# print(l)



# d=pd.DataFrame()
# print(d)

# l=["im","a","develper"]
# d=pd.DataFrame(l)
# print(d)

# d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# df=pd.DataFrame(d,columns=['A','B','C'])
# print(df)

di={'name'  :["a","b","c","d"],
    'degree':["BA","BCA","BBA","BCom"],
    'score' :[90,80,40,60],
    'age'   :[1,2,3,4]}
df=pd.DataFrame(di)
print(df)
# print(df[['name','score']])
# print(df[(df['score']>70) & (df['degree']=='BA')])
# print(pd.concat([df.head(2)]))
# print(pd.concat([df.tail(2)]))
# df['double_score']=np.multiply(df['score'],2)
# print(df)
# df['sqrt']=np.sqrt(df['age'])
# print(df)
sort=df.sort_values('score')
print(sort)

# d1={'ID':[1,2,3],'Name':["cat","dog","rat"]}
# d2={'ID':[2,3,4],'Age':[23,24,25]}
# d11=pd.DataFrame(d1)
# d22=pd.DataFrame(d2)
# print(pd.merge(d11,d22,on='ID'))

# d={'fscore':[10,20,np.nan,30],
#    'sscore':[40,50,60,np.nan],
#    'tscore':[np.nan,70,80,90],
#    'fscore':[100,200,300,400]}
# df=pd.DataFrame(d)
# print(df.isnull())
# print(df.fillna(df.mean()))
# print(df.dropna())
# print(df)

# df=pd.read_csv("people_data.csv")
# print(df)

# df=pd.read_csv("people_data.csv",usecols=["First Name","Email"])
# print(df)

# df=pd.read_csv("people_data.csv",index_col="First Name")
# print(df)

# df=pd.read_csv('people_data.csv',nrows=3)
# print(df)

data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Values': [100, 200, 300, 400, 500, 600]}
df=pd.DataFrame(data)
mean=df.groupby('Category')['Values'].mean()
print(mean)
print(df.rename(columns={'Category':'Cat','Values':'val'}))
print(df.transpose())