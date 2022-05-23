import os
import requests

URL_BASE="https://api.rawg.io/api/"
key=os.environ["exportkey"]
payload = {'key':key,'search':'Nintendo'}
r=requests.get(URL_BASE+'developers',params=payload)
if r.status_code == 200:
    doc=r.json()
    #print(doc)
    for p in doc["results"]:
        print (str(p["name"])+" - "+str(p["id"]))