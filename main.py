import requests

api_key = "pub_c127641ebc1b4a1aac153d1287725a7b"

url = " https://newsdata.io/api/1/latest?apikey=pub_c127641ebc1b4a1aac153d1287725a7b&q=pizza"

request = requests.get(url)
content = request.json()

print(content)