import requests
import os

#Busca los juegos de Nintendo y Playstation del último año y pon su nombre y notas de metacritic.
URL_BASE="https://api.rawg.io/api/"
key=os.environ["exportkey"]
payload = {'key':key,'dates':'2022-01-01,2022-05-16','platforms':'18,7'}
r=requests.get(URL_BASE+'games',params=payload)
if r.status_code == 200:
    doc=r.json()
    #print(json.dumps(doc, indent=1))
    for p in doc["results"]:
        print (str(p["name"])+" - "+str(p["metacritic"]))



#Muestra el nombre e id de los distribuidores de la empresa Nintendo
URL_BASE="https://api.rawg.io/api/"
key=os.environ["exportkey"]
payload = {'key':key,'search':'Nintendo'}
r=requests.get(URL_BASE+'developers',params=payload)
if r.status_code == 200:
    doc=r.json()
    #print(doc)
    for p in doc["results"]:
        print (str(p["name"])+" - "+str(p["id"]))


#Muestra los juegos más valorados de Nintendo por los usuarios.
URL_BASE="https://api.rawg.io/api/"
key=os.environ["exportkey"]
payload = {'key':key,'ordering':'-rating','platforms':'7'}
r=requests.get(URL_BASE+'games',params=payload)
if r.status_code == 200:
    doc=r.json()
    #print(json.dumps(doc, indent=1))
    for p in doc["results"]:
        print (str(p["name"])+" - "+str(p["rating"]))

