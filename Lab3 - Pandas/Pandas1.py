import pandas as pd

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

df1 = pd.DataFrame(x)

print(df1)
ids = df1[['ID']]
print(type(ids))

data = {'Student': ['David', 'Samuel', 'Terry', 'Evan'], 'Age': [27, 24, 22, 32], 'Country': ['UK', 'Canada', 'Japan', 'USA'], 'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 'Marks': [85, 72, 89, 76]}

df2 = pd.DataFrame(data)
b = df2[['Marks']]
print(b)
print(df2)

c = df2[['Country', 'Course']]
print(c)

d = df2['Student']
print(d)
print()
print(df2.loc[0, 'Course'])

print(df2.iloc[0:2, 0:3])

print(df2.loc[0:2, 'Age': 'Course'])


