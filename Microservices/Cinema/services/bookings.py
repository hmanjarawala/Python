# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:13:15 2020

@author: Himanshu.Manjarawala
"""

#from services import root_dir, nice_json
from flask import Flask, __version__
import os
import json
#from werkzeug.exceptions import NotFound

app = Flask(__name__)

print("Flask {}".format(__version__))

with open("{}\\db\\bookings.json".format(os.path.dirname(os.path.realpath(__file__ + '/..'))), "r") as f:
    bookings = json.load(f)
    print(any(booking['id'] == 5 for booking in bookings))


def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "bookings": "/bookings",
            "booking": "/bookings/<username>"
        }
    })


@app.route("/bookings", methods=['GET'])
def booking_list():
    return nice_json(bookings)


if __name__ == "__main__":
    app.run()