import pandas as pd
import requests
import json

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)
df = pd.DataFrame(results)
print(df[["name", "nutritions"]])

df2 = pd.json_normalize(results)
print(df2)

cherry = df2.loc[df2["name"] == "Cherry"]
print(cherry)
