from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

def load_quotes():
    with open("quotes.json", "r") as file:
        return json.load(file)

@app.route("/")
def home():
    return "Welcome to the Quote API! Try /quote"

@app.route("/quote", methods=["GET"])
def get_quote():
    quotes = load_quotes()
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(debug=True)
