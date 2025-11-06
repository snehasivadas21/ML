import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# x=[10,20,30,40]
# y=[20,25,35,55]

# plt.plot(x,y,color='green',linewidth=3,marker='o',markersize=15,linestyle='--')
# plt.title("Line Chart")
# plt.ylabel('Y-Axis')
# plt.xlabel('X-Axis')
# plt.show()

# x=["Thur","Fri","Sat","Sun"]
# y=[170,120,250,190]

# plt.bar(x,y,color='green',edgecolor='black',linewidth=2)
# plt.title("Bar Chart")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")
# plt.show()

# x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
#      21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]

# plt.hist(x,bins=10,color='steelblue',edgecolor='blue',linestyle='--',alpha=0.5)
# plt.title("Histogram")
# plt.xlabel("Total Bill")
# plt.ylabel("Frequency")
# plt.show()

# x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
# y = [170, 120, 250, 190, 160, 130, 240, 200]

# plt.scatter(x,y)
# plt.title("Scatter Plot")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")
# plt.show()

# cars=['AUDI','BMW','TESLA','FORD']
# data=[23,10,35,15]

# plt.pie(data,labels=cars)
# plt.title("Pie Chart")
# plt.show()


# df=sns.load_dataset('titanic')
# df.head()
# print(df.info())
# print(df.describe())
# print(df.shape)

#data cleaned
# df.isnull().sum()
# df['age']=df['age'].fillna(df['age'].median())
# df['embark_town']=df['embark_town'].fillna(df['embark_town'].mode()[0])
# df=df.drop(columns=['deck'])

#univariate analysis
# sns.histplot(df['age'],kde=True)
# plt.title("Age Distribution")
# plt.show()

# sns.histplot(df['fare'],kde=True)
# plt.title("Fare Distribution")
# plt.show()

#bivariate analysis
# plt.scatter(df['age'],df['fare'])
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.title("AGE VS FARE")
# plt.show()

# sns.barplot(x='sex',y='survived',data=df)
# plt.title("Survival Rate by Gender")
# plt.show()

# print(df.groupby('sex')['survived'].mean())
# print(df.groupby('class')['survived'].mean())
# print(df.groupby('embark_town')['survived'].mean())

# sns.boxplot(x='fare',data=df)
# plt.title("Fare Outliers")
# plt.show()

df=sns.load_dataset('tips')
df.head()
print(df.info())
print(df.describe())

print(df.isnull().sum())

sns.histplot(df['total_bill'],kde=True)
plt.title("Total Bill")
plt.show()
sns.histplot(df['tip'],kde=True)
plt.title("Tip")
plt.show()

plt.scatter(df["total_bill"],df["tip"])
plt.title("Total_bill vs Tip")
plt.xlabel("total_bill")
plt.ylabel("bill")
plt.show()

sns.boxplot(x="total_bill",data=df)
plt.title("Total Bill")
plt.show()

print(df.groupby('day')['tip'].mean())
print(df.groupby('sex')['total_bill'].sum())
df['tip_percentage']=df['tip']/df['total_bill']*100
print(df.groupby('smoker')['tip_percentage'].mean())