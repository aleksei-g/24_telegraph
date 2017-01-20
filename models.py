from server import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column('post_id', db.Integer, primary_key=True)
    header = db.Column(db.String(100))
    signature = db.Column(db.String(50))
    body = db.Column(db.Text)
    user_id = db.Column(db.String(48))

    def __init__(self, header, signature, body, user_id):
        self.header = header
        self.signature = signature
        self.body = body
        self.user_id = user_id
