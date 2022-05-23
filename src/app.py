from crypt import methods
from imaplib import IMAP4_stream
import json
from operator import itemgetter
from flask import Flask, request
from src.services.db.schema import UserItemSchema
from src.config import CONFIG_BY_ENV
from loguru import logger
from src.services.db.models import UserItem, db
import os


from flask import Flask, jsonify

CFG = CONFIG_BY_ENV[os.getenv("FLASK_ENV", "local")]
DB_URI = f"{CFG.DB_TYPE}://{CFG.DB_USER}:{CFG.DB_PASS}@{CFG.DB_HOST}:{CFG.DB_PORT}/{CFG.DB_NAME}"

app = Flask(__name__)

app.config["DEBUG"] = CFG.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI

db.init_app(app)
with app.app_context():
    logger.info("Creating all tables...")
    db.create_all()
    logger.info("Created tables..")

@app.route("/sample/api/v1/", methods=["GET"])
def sample():
    message = "Hello I am uday kumar, welcome to python"
    return jsonify({"message": message})

@app.route("/sample/api/v1/user/", methods=["POST"])
def addUser():
    data = request.json
    try:
        item = UserItem(**data)
        db.session.add(item)
        db.session.commit()
        logger.info("User Record inserted successfully")
    except:
        logger.error("Error Occurred while inserting user record")
    return jsonify(data)

@app.route("/sample/api/v1/user/<id>/", methods=["GET"])
def getUser(id: str):
    res = ""
    try:
        res = UserItem.query.filter_by(id=id).first()
        res = UserItemSchema().dump(res)
        logger.info("User Record fetched successfully")
    except:
        logger.error("Error occurred while retrieving records")
    
    return jsonify(res)

@app.route("/sample/api/v1/user/", methods=["GET"])
def getUsers():
    res = ""
    try:
        users = UserItem.query.all()
        res = UserItemSchema(many=True).dump(users)
        logger.info("User Records fetched successfully")
    except:
        logger.error("Error occurred while retrieving records")
    
    return jsonify(res)
    
@app.route("/sample/api/v1/user/<id>/", methods=["DELETE"])
def deleteUser(id: str):
    res = ""
    try:
        item = UserItem.query.filter_by(id=id).first()
        db.session.delete(item)
        db.session.commit()
        logger.info("User Record delted successfully")
    except:
        logger.error("Error occurred while deleting record")
    res = UserItemSchema().dump(item)
    return jsonify(res)