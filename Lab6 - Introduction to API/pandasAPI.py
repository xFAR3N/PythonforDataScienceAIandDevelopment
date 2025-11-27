import pandas as pd
import matplotlib.pyplot as plt

dict = { "a": [11, 21, 31], 'b': [12, 22, 32]}

df = pd.DataFrame(dict)

type(df)
print(df.head())
print(df.mean())