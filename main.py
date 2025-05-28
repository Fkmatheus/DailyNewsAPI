import requests
from send_email import send_email

api_key = "pub_c127641ebc1b4a1aac153d1287725a7b"

url = "https://newsdata.io/api/1/latest?apikey=pub_c127641ebc1b4a1aac153d1287725a7b&q=pizza"

request = requests.get(url)
content = request.json()

#print(content["results"])

body = ""
cont = 0
for x in content["results"]:
    if content["results"][cont]["title"] != None and content["results"][cont]["description"] != None and content["results"][cont]["link"] != None:
        body = body + content["results"][cont]["title"] + "\n" + content["results"][cont]["description"] + "\n" + content["results"][cont]["link"] + 2*"\n"

    cont += 1

body = body.encode("utf-8")
send_email(body)

