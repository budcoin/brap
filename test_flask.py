from pymongo import MongoClient
from flask import Flask
from flask import render_template


client = MongoClient()
db = client.brap_database
sessionsdata = db.sessionsdata

app = Flask(__name__)

@app.route("/")
def session():
    columns = ['tempf', 'tempr', 'fronts', 'rears', 'gx', 'gy', 'gz', 'ax', 'ay', 'az']
    return render_template('session.html', sessionsdata=sessionsdata, columns=columns)

if __name__ == "__main__":
    app.run()
