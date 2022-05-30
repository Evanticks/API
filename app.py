import requests
from datetime import date
import os
from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")

@app.route('/lista_juegos',methods=["POST"])
def lista_juegos():
    URL_BASE="https://api.rawg.io/api/"
    key=os.environ["exportkey"]
    #Lo hago con datetime porque la librería os.system no guarda en una variable la fecha.
    texto=request.form.get("texto")
    texto2=request.form.get("texto2")
    texto3=request.form.get("texto3")
    if texto != None and texto != "":
        hoy=date.today()
        fecha=str(texto)+','+str(hoy)
        payload = {'key':key,'dates':fecha,'platforms':'18,7'}
        r=requests.get(URL_BASE+'games',params=payload)
        if r.status_code == 200:
            doc=r.json()
            juegos=[]
#            texto=request.form.get("texto")
            for dato in doc.get("results"):
                nombre=str(dato.get("nombre"))
                diccionario={"name":dato.get("name"),"metacritic":dato.get("metacritic"),"background_image":dato.get("background_image"),"slug":dato.get("slug")}
                juegos.append(diccionario)
            return render_template("lista_juegos.html",juegos=juegos,texto=texto)
        else:
            return abort (404)
    if texto3 != None and texto2 != "":
        payload = {'key':key,'search':str(texto2)}
        r=requests.get(URL_BASE+'games',params=payload)
        if r.status_code == 200:
            doc=r.json()
            juegos=[]
            for dato in doc.get("results"):
                nombre=str(dato.get("name"))
                if nombre.startswith(texto2):
                    diccionario={"name":dato.get("name"),"metacritic":dato.get("metacritic"),"background_image":dato.get("background_image"),"slug":dato.get("slug")}
                    juegos.append(diccionario)
            return render_template("lista_juegos.html",juegos=juegos)
        else:
            return abort (404)
    if texto3 != None and texto3 != "":
        payload = {'key':key,'search':str(texto3)}
        r=requests.get(URL_BASE+'developers',params=payload)
        if r.status_code == 200:
            doc=r.json()
            print(doc)
            juegos=[]
            for dato in doc.get("results"):
                nombre=str(dato.get("name"))
                if nombre.startswith(texto3):
                    diccionario={"name":dato.get("name"),"id":dato.get("id"),"slug":dato.get("slug")}
                    juegos.append(diccionario)
                    print(diccionario)
            return render_template("desarrollador.html",juegos=juegos,texto3=texto3)    
        else:
            return abort (404)
    else:
        return abort (404)
@app.route('/juego/<slug>')
def juego(slug):
    URL_BASE="https://api.newscatcherapi.com/v2/search"
    key=os.environ["exportkey2"]
    headers= {'x-api-key': key}
    payload = {'q':slug}
    r=requests.get(URL_BASE,params=payload,headers=headers)
    if r.status_code == 200:
        doc=r.json()
        print(doc)
        juegos=[]
        for dato in doc.get("articles"):
            #titular=str(dato.get("title"))
            idioma=str(dato.get("language"))
            if idioma == ("es"):
                diccionario={"title":dato.get("title"),"summary":dato.get("summary")}
                print(diccionario)
                juegos.append(diccionario)
            else:
                return abort (404)
        #print(json.dumps(doc, indent=1))
        #for p in doc["results"]:
        #    print (str(p["name"])+" - "+str(p["metacritic"]))
        return render_template("juego.html",juegos=juegos)


#https://api.rawg.io/docs/
port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)
#app.run("0.0.0.0",5000,debug=True)