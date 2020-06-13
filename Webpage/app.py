from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/embed")
def embed():
    return render_template("embed.html")

if __name__ == "__main__":
    app.run(debug=True)