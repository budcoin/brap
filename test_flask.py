import pymongo
from pymongo import MongoClient
from flask import Flask

client = MongoClient()
db = client.brap_database
sessionsdata = db.sessionsdata

app = Flask(__name__)

@app.route("/")
def hello():
    return str(sessionsdata.find_one())

if __name__ == "__main__":
    app.run()