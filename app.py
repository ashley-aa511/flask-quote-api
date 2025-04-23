from flask import Flask, jsonify, request
from models import db, Quote
import random
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def load_quotes():
    with open("quotes.json", "r") as file:
        return json.load(file)
    
# Create the DB and add some sample data

def create_tables():
    db.create_all()
    if Quote.query.count() == 0:
        sample_quotes = [
            Quote(author="Maya Angelou", quote="You will face many defeats in life, but never let yourself be defeated."),
            Quote(author="Nelson Mandela", quote="It always seems impossible until it’s done."),
            Quote(author="Albert Einstein", quote="Life is like riding a bicycle. To keep your balance you must keep moving.")
        ]
        db.session.bulk_save_objects(sample_quotes)
        db.session.commit()

@app.route("/")
def home():
    return "Welcome to the Quote API! Try /quote"

@app.route("/quote", methods=["GET"])
def get_quote():
    quotes = load_quotes()
    return jsonify(random.choice(quotes))

@app.route("/quote", methods=["POST"])
def add_quote():
    data = request.get_json()
    author = data.get("author")
    quote_text = data.get("quote")

    if not author or not quote_text:
        return jsonify({"error": "Both 'author' and 'quote' are required."}), 400

    new_quote = Quote(author=author, quote=quote_text)
    db.session.add(new_quote)
    db.session.commit()
    return jsonify(new_quote.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True)
