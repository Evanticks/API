import requests
import os
from flask import Flask, render_template, request
app = Flask(__name__)


#Busca los juegos de Nintendo y Playstation del último año y pon su nombre y notas de metacritic.
#URL_BASE="https://api.rawg.io/api/"
#key=os.environ["exportkey"]
#payload = {'key':key,'dates':'2022-01-01,2022-05-16','platforms':'18,7'}
#r=requests.get(URL_BASE+'games',params=payload)
#if r.status_code == 200:
#    doc=r.json()
#    #print(json.dumps(doc, indent=1))
#    #for p in doc["results"]:
#    #    print (str(p["name"])+" - "+str(p["metacritic"]))

@app.route('/')
def inicio():
    return render_template("inicio.html")

#@app.route('/lista_juegos')
#def lista_juegos():
#    URL_BASE="https://api.rawg.io/api/"
#    key=os.environ["exportkey"]
#    payload = {'key':key,'dates':'2022-01-01,2022-05-16','platforms':'18,7'}
#    r=requests.get(URL_BASE+'games',params=payload)
#    if r.status_code == 200:
#        doc=r.json()
#        juegos=[]
#        texto=request.form.get("texto")
#        for dato in doc.get("results"):
#            nombre=str(dato.get("nombre"))
#            if nombre.startswith(texto):
#                diccionario={"name":dato.get("name"),"metacritic":dato.get("metacritic"),"background_image":dato.get("background_image")}
#                juegos.append(diccionario)
#        return render_template("lista_juegos.html",juegos=juegos)

#@app.route('/juego/<id>')
#def juego(id):
#    for dato in datos:
#        if dato.get("id") == int(id):
#            return render_template("juego.html",dato=dato)

##Muestra el nombre e id de los distribuidores de la empresa Nintendo
#URL_BASE="https://api.rawg.io/api/"
#key=os.environ["exportkey"]
#payload = {'key':key,'search':'Nintendo'}
#r=requests.get(URL_BASE+'developers',params=payload)
#if r.status_code == 200:
#    doc=r.json()
#    #print(doc)
#    for p in doc["results"]:
#        print (str(p["name"])+" - "+str(p["id"]))
#
#
##Muestra los juegos más valorados de Nintendo por los usuarios.
#URL_BASE="https://api.rawg.io/api/"
#key=os.environ["exportkey"]
#payload = {'key':key,'ordering':'-rating','platforms':'7'}
#r=requests.get(URL_BASE+'games',params=payload)
#if r.status_code == 200:
#    doc=r.json()
#    #print(json.dumps(doc, indent=1))
#    for p in doc["results"]:
#        print (str(p["name"])+" - "+str(p["rating"]))
#
#https://api.rawg.io/docs/

app.run("0.0.0.0",5000,debug=True)