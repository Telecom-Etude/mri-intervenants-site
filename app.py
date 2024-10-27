import json
from flask import Flask, render_template, request, redirect, make_response, send_from_directory
import database

app = Flask(__name__)
@app.route("/")
def index():
    return app.send_static_file("html/main.html")


if __name__ == '__main__':
    app.run(debug=False,port=80,host="0.0.0.0") #Lance l'application