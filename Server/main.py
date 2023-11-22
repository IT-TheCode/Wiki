from flask import Flask
from flask import render_template
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
host = s.getsockname()[0]
s.close()

port = 100

app = Flask(__name__)

@app.route("/test.html")
def test():
    return render_template("test.html")

@app.route("/links.html")
def links():
    return render_template("links.html")

@app.route("/picture.html")
def picture():
    return render_template("picture.html")

@app.route("/impressum.html")
def impressum():
    return render_template("impressum.html")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    print("Website started")
    print("IP:",host, ":", port, sep='')
    app.run(debug=True, host=host, port=port)

