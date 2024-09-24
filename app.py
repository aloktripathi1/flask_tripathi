from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index_1.html")

@app.route("/menu")
def menu():
    return "<h1> Chai -- Rs 10 </h1> <br> <h1> Vodka -- Rs 100 </h1> <br> <h1> Scotch -- Rs 200 </h1> <br> <h1> Pauaa -- Rs 39 </h1>"






if __name__ == "__main__":
    app.run(debug = True)
