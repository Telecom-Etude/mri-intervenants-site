import json
from flask import Flask, render_template, request, redirect, make_response, send_from_directory
import database

with open('secret.txt','r',encoding='utf-8') as f:
    secret = f.readline()

app = Flask(__name__)
@app.route("/")
def index():
    return app.send_static_file("html/main.html")

@app.route("/ping",methods=["GET","POST"])
def ping():
    try:
        data = request.get_json()
        print(data)
    except:
        print("Pas de donnée dans la request")
    return "pong"

@app.route("/get_mri",methods=["GET","POST"])
def get_mri():
    mris=database.get_mris()
    result_list=[database.cleanResult(mri) for mri in mris]
    return json.dumps(result_list)

@app.route('/new',methods=["POST"])
def new_mri():
    try:
        data = request.get_json()
        if data["secret"] != secret:
            print("Erreur de secret")
            return "Unauthorized"
        print("Accepté")
        database.insert_mri(data["body"])
    except Exception as e:
        print(e)
        print("Pas de donnée dans la request")
        return "Error"
    return "OK"

@app.route("/view/<identifier>",methods=["GET"])
def view(identifier):
    mri = database.getMri(identifier)
    if mri=="":
        app.redirect("/",404)
    return render_template("view.html",html=mri['mri'],title=mri['title'])

if __name__ == '__main__':
    app.run(debug=False,port=8080,host="0.0.0.0") #Lance l'application

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")