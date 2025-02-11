import pandas as pd
df=pd.read_csv("people.csv")
print(df)
print(df['Name'])
print(df[['Name']]) # use [[]] for 2-D data

# select row by index

print(df.iloc[0])
print(df.iloc[1:2])

# # using condition
print(df[df['Age']>25])

# add new column
df['salary']=[40000,25000,30000,27000,26500]
print(df)

df = pd.read_csv("shopping_trends.csv")
print(df.head(10))
print(df.isnull().sum())


## Dataframe

df=pd.DataFrame({'Yes':[50,24,30],'No':[10,6,15]})
print(df)

df1=pd.DataFrame({'Bob':['i like it','it was awful'],'jack':['good','not good']},index=['Product A','Product B'])
print(df1)


# # series

df2=pd.Series([1,5,4,8,9,6])
print(df2)

data=pd.read_csv('shopping_trends.csv')
print(data.shape)
print(data.head())
print(data.tail())
print(data.Location)
print(data['Location'][2])


# # # indexing 
# # # index based selection (iloc())
print(data.iloc[0]) # selecting first index
print(data.iloc[1:3,2]) # 1:3 slects index and ,2 selects row which we want

print(data.iloc[[0,1,2],0:3])

print(data.iloc[-5:])


# # label based selection (loc())
print(data.loc[3898,'Location'])
print(data.loc[:,['Season','Location','Category']])

# # # conditional selection

print(data.Location=='Minnesota')

print(data.loc[data.Location=='Minnesota'])

print(data.loc[(data.Location=='Minnesota') & (data.ReviewRating>=2.5)])

print(data.ReviewRating.describe())
print(data.isna().sum())
print(data.isnull().sum())
print("Max Number of Row is :",pd.options.display.max_rows) 
print(data.info())
print(data.duplicated().sum()) # show all duplicate values present in dataset
dropDuplicate=data.drop_duplicates() # remove all duplicate value form dataset
print(dropDuplicate)

cor=data['ReviewRating'].corr(data['PreviousPurchases'])
print(cor)