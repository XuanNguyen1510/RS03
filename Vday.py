from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yes.html")
def yes():
    return render_template("yes.html")

if __name__ == "__main__":
    app.run(debug=True)
