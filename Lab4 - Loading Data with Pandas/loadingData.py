import pandas as pd

csv_path = 'Product_sales.csv'
df = pd.read_csv(csv_path)

print(df.head())

xlsx_path = 'Product_sales.xlsx'
df2 = pd.read_excel(xlsx_path)

print(df2.head())

x = df[['Quantity']]
print(x)

x = df['Product']
print(x)

y = df[['Product', 'Quantity', 'Category']]
print(y)

print(df.iloc[0, 0])
print(df.iloc[1, 0])

print(df.iloc[0,2])
print(df.iloc[1,2])

print(df.loc[1, 'Total'])
print(df.loc[0, 'Product'])

print(df.iloc[1:3, 0:5])

print(df.loc[0:4, 'Product':'OrderDate'])
print(y.loc[0:4, 'Product'])

new_index=['a', 'b', 'c', 'd', 'e']

df_new = df
df_new.index = new_index
print(df_new.head())