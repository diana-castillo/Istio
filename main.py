from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        url = "https://dog.ceo/api/breeds/image/random"
    
    if request.method == 'POST':
        name = request.form['name']
        url = "https://dog.ceo/api/breed/{}/images/random".format(name)
   
    resultado = requests.get(url)
    datos = resultado.json()
    imagen = datos["message"]

    return render_template("index.html", imagen=imagen)


app.run(host="0.0.0.0", port=8080)