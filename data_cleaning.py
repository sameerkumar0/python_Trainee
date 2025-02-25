import pandas as pd

# Create a sample dataset
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, None],
    "Name": ["Alice", "Bob", "Charlie", None, "Eve", "Frank", "Grace", "Hank", "Ivy", "Jake"],
    "Age": [25, 30, None, 40, 29, 35, None, 50, 22, 28],
    "Gender": ["Female", "Male", "Male", "Female", None, "Male", "Female", "Male", "Female", "Male"],
    "Salary": [50000, 60000, 70000, None, 65000, 58000, 72000, 52000, 68000, None],
    "Join_Date": ["2021-05-21", "2020-06-15", None, "2019-08-10", "2022-01-01",
                  "2018-11-23", "2021-02-14", None, "2017-09-30", "2016-12-05"],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", None, "Dallas"]
}

df = pd.DataFrame(data)

# Display dataset
print(df)



# handling missing value
# print(df.isnull().sum())

# dropping mising value

# df.dropna(inplace=True)
# print(df)


# filling missing values

# df['Age'] = df['Age'].fillna(df['Age'].median()) # inplace=True use to modify the original dataframe
# df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# print(df)


# correcting data type

# df['Customer_ID']=df['Customer_ID'].astype('int64') # convert to integer
# df['Join_Date']=pd.to_datetime(df['Join_Date']) # convert to datetime

# print(df)



# handling Outlier

Q1=df['Salary'].quantile(0.25)
Q3=df['Salary'].quantile(0.75)
IQR=Q1-Q3
print(IQR)

# removing outlier

df=df[(df['Salary']>=Q1-1.5*IQR) & (df['Salary'] <= Q3 + 1.5 * IQR)]
print(df)