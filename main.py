from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landingPage():
   return render_template(".html")
@app.route("/Shop")
def shopPage():
    return render_template(".html")

if __name__ == '__main__':
    app.run(debug=True)