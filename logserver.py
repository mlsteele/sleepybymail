"""
Listen and log arbitrary stuff.
"""

import datetime
import pymongo
import quickieconfig as qc
from flask import Flask, request

SERVER_DEBUG_MODE = qc.param("SERVER_DEBUG_MODE") in ["ON", "YES", "TRUE", "1", 1]
MONGO_DB = qc.param("MONGO_DB")

app = Flask(__name__)
mongo_client = pymongo.MongoClient()
mongo_db = mongo_client[MONGO_DB]

@app.route("/")
def root():
    return "Hey there."

@app.route("/heartbeat")
def heartbeat():
    return "Still alive."

@app.route("/log")
def receive_log():
    data = _unmultidict(request.args)
    data["time_logged"] = datetime.datetime.now()
    _add_log_entry(data)
    return "Ok."

def _unmultidict(multidict):
    """
    Convert a multidict back to a normal dict.
    Assume the first value of each entry.
    """
    d = {}
    for key in dict(multidict):
        d[key] = multidict[key]
    return d

def _add_log_entry(event):
    """Log an event to mongo."""
    mongo_db.events.insert(event, j=True)

if __name__ == "__main__":
    app.debug = SERVER_DEBUG_MODE
    app.run(port=qc.param("LOG_SERVER_PORT"))
