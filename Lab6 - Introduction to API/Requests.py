import requests
import os
from PIL import Image
from IPython.display import IFrame


url = 'https://www.ibm.com/'

response = requests.get(url)
print(response.status_code)
print(response.headers)
date = response.headers['Date']
#for key in response.headers:
    #print(key,': ', response.headers[key], sep='')


new_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r = requests.get(new_url)

print(r.status_code)
print(r.headers['content-type'])

path = os.path.join(os.getcwd(), 'image.png')
with open(path, 'wb') as f:
    f.write(r.content)

Image.open(path)

url_get = 'http://httpbin.org/get'

payload = {'name': 'Joseph', 'ID': '123'}

r_get = requests.get(url_get, params=payload)
print("GET URL:",r_get.url)

print('GET Request body:', r.request.body)

url_post = 'http://httpbin.org/post'

r_post = requests.post(url_post, data=payload)
print("POST request URL:", r_post.url)
print('POST Request body:', r_post.request.body)