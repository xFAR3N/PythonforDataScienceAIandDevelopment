import json

import pandas as pd
import requests

url = 'https://official-joke-api.appspot.com/jokes/ten'

response = requests.get(url)
data = json.loads(response.text)
df = pd.DataFrame(data)
df.drop(columns=['type', 'id'], inplace=True)
print(df)
