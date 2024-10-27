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

@app.route('/new',methods=["POST"])
def new_mri():
    try:
        data = request.get_json()
        if data["secret"] != secret:
            return "Unauthorized"
        print("Accepté")
    except:
        print("Pas de donnée dans la request")
        return "Error"
    return "OK"


if __name__ == '__main__':
    app.run(debug=False,port=80,host="0.0.0.0") #Lance l'application