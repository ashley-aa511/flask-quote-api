# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    quote = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "quote": self.quote
        }
