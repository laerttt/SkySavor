from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landingPage():
   return render_template("index.html")
@app.route("/Shop")
def shopPage():
    return render_template(".html")

FLASK_ENV="development"
FLASK_APP="main.py"


if __name__ == '__main__':
    app.run(debug=True)