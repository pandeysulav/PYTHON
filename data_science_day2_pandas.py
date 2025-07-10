import numpy as np

# reshape
# 1-D to 2-D
a =np.array([1,2,3,4,5,6,7,8,9,10,11.12])
print(a)
b = a.reshape(2,3,2)#order(4.3)
print(b)

# dtype
test1 = np.array([1,2,3,0,4,5])
test2 = test1.astype('i')
print('final', test2)
print(test2.dtype)

# shape
data = np.array (((1,2,3,4), (4,5,6,7)))
print(data.shape)

import pandas as pd
print(pd.__version__)

dataset = {
    'cars':['Hyundai','Tesla','Ferrari','Mercedes','Toyota'],
    'price':[4,3,2,6,7]
}
print(dataset)
result = pd.DataFrame(dataset)
print(result)

# Series (like column in a table)
x = [1,3,5,7,9]
result = pd.Series(x,index=['a','b','c','d','e'])
print(result)


dataset = {
    'cars': 'Tesla',
    'price':'5 crores',
    'owner' : 'Musk'
}
print(dataset)
result = pd.Series(dataset)#Series = represents single axis
print(result)

# Cleaning empty cells
# Remove rows
# Data cleaning means fixing bad data from your dataset
# Bad data could be: data in wrong format, duplicates, empty cells, nan(not available number)
# It will you give you wrong results always, due to this we will have to remove the rows

df = pd.read_csv(r'C:\Users\A S U S\OneDrive\Documents\OneDrive\Desktop\data.csv',encoding = 'unicode_escape')
print(df.info())


Never work on the original file
df1 = df.dropna() #drop or remove not available data(entire row)
print(df.info())
df['Calories'].fillna(400,inplace=True)#Inplace = True, same dataframe update
print(df.to_string())
mean_value = df['Calories'].mean()
print(mean_value)
df['Calories'].fillna(400,inplace=True)#Inplace = True, same dataframe update
print(df.to_string())
print(df.info)
median_value = df['Pulse'].mean()
print(median_value )
df['Pulse'].fillna(median_value ,inplace=True)#Inplace = True, same dataframe update
print(df.to_string())
print(df.info())
df['Date'] = pd.to_datetime(df['Date'], format = 'mixed', errors ='coerce')
print(df.dtypes)

