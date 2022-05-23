from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

TABLE_PREFIX = "user_"

class UserItem(db.Model):

    __tablename__ = f"{TABLE_PREFIX}user_item"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    age = db.Column(db.BIGINT)
    gender = db.Column(db.String)
    address = db.Column(db.String)




